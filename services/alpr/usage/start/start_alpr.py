"""
Created By: ishwor subedi
Date: 2024-02-07
"""

import os
from PIL import Image
from paddleocr.tools.infer.utility import draw_ocr

from services.alpr.src.entity.service_config import RecognitionConfig
from services.alpr.src.services.recognition.paddleocr_service import PaddleocrService

from services.alpr.usage import alpr_logger
import threading
import time

ALPR_LOGGER = alpr_logger()


class StartAlprExample:
    def __init__(self, det_model, recognition_model, rec_char_dict, detected_img_dir, output_path, flag_path):
        config = RecognitionConfig(det_model=det_model, recognition_model=recognition_model,
                                   rec_char_dict=rec_char_dict)
        self.latest_image_path = None
        time.sleep(2)
        self.paddle_ocr = PaddleocrService(config)
        self.alpr_start = False
        self.detected_img_dir = detected_img_dir
        self.rec_output_path = output_path
        self.non_rec_output_path = 'services/alpr/output/paddleocr_non_rec_output'
        self.flag_path = flag_path
        self.running = False

    def start_alpr(self):
        self.start_alpr_service = threading.Thread(target=self.main_alpr_service)
        self.start_alpr_service.start()
        self.running = True

    def save_image_thread(self, output_path, boxes, txts, scores):
        self.save_thread = threading.Thread(target=self.rec_save_image, args=(output_path, boxes, txts, scores))
        self.save_thread.start()

    def stop_image_thread(self, output_path, boxes, txts, scores):
        self.stop_thread = threading.Thread(target=self.non_rec_save_image, args=(output_path, boxes, txts, scores))
        self.stop_thread.start()

    def stop_alpr(self):
        self.running = False
        if self.start_alpr_service.is_alive():
            self.start_alpr_service.join()
        ALPR_LOGGER.info("ALPR service successfully stopped.")

    def rec_save_image(self, output_path, boxes, txts, scores):
        try:
            if len(boxes) == 0:
                img = Image.open(self.latest_image_path)
                img.save(output_path)

            else:
                img = Image.open(self.latest_image_path)

                img = draw_ocr(img, boxes, txts, scores, font_path='services/alpr/resources/fonts/nepali.ttf')
                img = Image.fromarray(img)

                img.save(output_path)

        except Exception as e:
            ALPR_LOGGER.error(f"Error saving image: {e}")

    def non_rec_save_image(self, output_path):
        try:
            img = Image.open(self.latest_image_path)
            img.save(output_path)
        except Exception as e:
            ALPR_LOGGER.error(f"Error saving image: {e}")

    def main_alpr_service(self, img):

        while self.running:
            list = sorted(os.listdir(img))

            for image in list:
                self.latest_image_path = os.path.join(img, image)
                time.sleep(0.5)
                try:
                    boxes, txts, scores = self.paddle_ocr.detection_recognition_cls(self.latest_image_path)
                    if len(txts or boxes) == 0:
                        output_path = os.path.join(self.non_rec_output_path, image)
                        self.non_rec_save_image(output_path)
                    else:
                        output_path = os.path.join(self.rec_output_path, image)
                        self.save_image_thread(output_path, boxes, txts, scores)
                    yield boxes, txts, scores

                except Exception as e:
                    ALPR_LOGGER.error(f"An error occurred: {e}")
                    yield [], [], []

                finally:
                    if os.path.exists(self.latest_image_path):
                        print(f"Removing image: {self.latest_image_path}")
                        os.remove(self.latest_image_path)
                        list.remove(image)

    def check_stop_flag(self):
        try:
            with open(self.flag_path, 'r') as file:
                flag = file.read().strip()
                print(f"Read stop flag: {flag}")  # print the value of the stop flag read from the file
                return flag == "True"
        except Exception as e:
            ALPR_LOGGER.error(f"Error checking stop flag: {e}")
            return False

    def create_stop_flag(self):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write('False')
        except Exception as e:
            ALPR_LOGGER.error(f"Error creating stop flag: {e}")

    def update_stop_flag(self, value):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write(str(value))
        except Exception as e:
            ALPR_LOGGER.error(f"Error updating stop flag: {e}")

    def start_service(self):
        try:
            self.running = True
            self.start_alpr()
            ALPR_LOGGER.info("ALPR service successfully started")
            stop_check_thread = threading.Thread(target=self.check_and_stop)
            stop_check_thread.start()
            while self.running:
                time.sleep(1)
                stop_flag = self.check_stop_flag()

                if stop_flag:
                    self.running = False
                    self.stop_alpr()
                    ALPR_LOGGER.info("ALPR service successfully stopped.")

        except Exception as e:
            ALPR_LOGGER.error(f"Error starting ALPR service: {e}")

    def check_and_stop(self):
        while self.running:
            time.sleep(1)
            stop_flag = self.check_stop_flag()
            print(f"Stop flag: {stop_flag}")  # print the value of the stop flag

            if stop_flag:
                print("Stopping the service...")  # print a message before stopping the service
                self.running = False
                self.stop_alpr()
                ALPR_LOGGER.info("ALPR service successfully stopped.")

    def stop_service(self):
        self.update_stop_flag("True")


if __name__ == '__main__':
    det_model = 'services/alpr/resources/paddleocr/Multilingual_PP-OCRv3_det_infer/'
    recognition_model = 'services/alpr/resources/paddleocr/custom_recog/'
    rec_char_dict = 'services/alpr/resources/paddleocr/devanagari_dict.txt'

    img = 'services/alpr/resources/plate_detected/'
    output_path = 'services/alpr/output/paddleocr_rec_output/'
    font_path = 'services/alpr/resources/fonts/nepali.ttf'
    flag_path = 'services/alpr/resources/flag_check/alpr_status.txt'
    start_alpr = StartAlprExample(det_model, recognition_model, rec_char_dict, img, output_path, flag_path)
    start_alpr.create_stop_flag()
    results_generator = start_alpr.main_alpr_service(img)
    for boxes, txts, scores in results_generator:
        print(f"Boxes: {boxes}")
        print(f"Texts: {txts}")
        print(f"Scores: {scores}")
