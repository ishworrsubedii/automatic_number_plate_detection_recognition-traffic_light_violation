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
from datetime import datetime


class StartAlprExample:
    def __init__(self, det_model, recognition_model, rec_char_dict, detected_img_dir, output_path, non_rec_output_path,
                 flag_path,
                 result_file, recognized_images_file_path, non_recognized_images_file_path):
        config = RecognitionConfig(det_model=det_model, recognition_model=recognition_model,
                                   rec_char_dict=rec_char_dict)
        self.latest_image_path = None
        time.sleep(2)
        self.paddle_ocr = PaddleocrService(config)
        self.alpr_start = False
        self.detected_img_dir = detected_img_dir
        self.rec_output_path = output_path
        self.non_rec_output_path = non_rec_output_path
        self.flag_path = flag_path
        self.running = False

        self.result = result_file  # recognized result file path
        self.recognized_images_file_path = recognized_images_file_path  # recognized images file path
        self.non_recognized_images_file_path = non_recognized_images_file_path  # non recognized images file path

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

                filename = os.path.basename(self.latest_image_path)

                # new_output_path = os.path.join(output_path, filename)

                with open('services/alpr/output/recognized_images_paths.txt', 'a') as file:
                    file.write(f"Recognized_image_path:{output_path}\n")

                img.save(output_path)

        except Exception as e:
            print(f"Error saving image: {e}")

    def non_rec_save_image(self, output_path):
        try:
            img = Image.open(self.latest_image_path)
            filename = os.path.basename(self.latest_image_path)

            new_output_path = os.path.join(output_path, filename)

            with open('services/alpr/output/non_recognized_images_paths.txt', 'a') as file:
                file.write(f"Non_Recognized_image_path:{output_path}\n")
            img.save(output_path)
        except Exception as e:
            print(f"Error saving image: {e}")

    def main_alpr_service(self):
        while self.running:
            list = sorted(os.listdir(self.detected_img_dir))  # Moved this line inside the loop

            for image in list:
                self.latest_image_path = os.path.join(self.detected_img_dir, image)
                time.sleep(0.5)
                try:
                    boxes, txts, scores = self.paddle_ocr.detection_recognition_cls(self.latest_image_path)
                    if len(txts or boxes) == 0:
                        output_path = os.path.join(self.non_rec_output_path, image)
                        self.non_rec_save_image(output_path)

                    else:
                        current_datetime = datetime.now()
                        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

                        with open('services/alpr/output/result.txt', 'a') as file:
                            average_score = sum(scores) / len(scores)
                            merged_text = ' '.join(txts)

                            file.write(
                                f" Image_path:{self.latest_image_path},Text: {merged_text}, Score: {average_score},Date_recognized:{formatted_datetime}\n")

                        output_path = os.path.join(self.rec_output_path, image)
                        self.save_image_thread(output_path, boxes, txts, scores)

                except Exception as e:
                    print(f"An error occurred: {e}")

                finally:
                    if os.path.exists(self.latest_image_path):
                        print(f"Removing image: {self.latest_image_path}")
                        os.remove(self.latest_image_path)
                        list.remove(image)

    def check_stop_flag(self):
        try:
            with open(self.flag_path, 'r') as file:
                flag = file.read().strip()
                return flag == "True"
        except Exception as e:
            print(f"Error checking stop flag: {e}")
            return False

    def create_stop_flag(self):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write('False')
        except Exception as e:
            print(f"Error creating stop flag: {e}")

    def update_stop_flag(self, value):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write(str(value))
        except Exception as e:
            print(f"Error updating stop flag: {e}")

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
                    print("ALPR service successfully stopped.")

        except Exception as e:
            print(f"Error starting ALPR service: {e}")

    def check_and_stop(self):
        while self.running:
            time.sleep(1)
            stop_flag = self.check_stop_flag()

            if stop_flag:
                print("Stopping the service...")  # print a message before stopping the service
                self.running = False
                self.stop_alpr()
                print("ALPR service successfully stopped.")

    def stop_service(self):
        self.update_stop_flag("True")


if __name__ == '__main__':
    det_model = 'services/alpr/resources/paddleocr/Multilingual_PP-OCRv3_det_infer/'
    recognition_model = 'services/alpr/resources/paddleocr/custom_recog/'
    rec_char_dict = 'services/alpr/resources/paddleocr/devanagari_dict.txt'

    images_directory = 'services/alpr/resources/plate_detected/'
    output_path = 'services/alpr/output/paddleocr_rec_output/'
    non_rec_output_path = 'services/alpr/output/paddleocr_non_rec_output'
    flag_path = 'services/alpr/resources/flag_check/alpr_status.txt'

    result_save_path = "services/alpr/output/result.txt"
    recognized_images_file_path = "services/alpr/output/recognized_images_paths.txt"
    non_recognized_images_file_path = "services/alpr/output/non_recognized_images_paths.txt"

    start_alpr = StartAlprExample(det_model=det_model, recognition_model=recognition_model, rec_char_dict=rec_char_dict,
                                  detected_img_dir=images_directory, output_path=output_path,
                                  non_rec_output_path=non_rec_output_path, flag_path=flag_path,
                                  result_file=result_save_path, recognized_images_file_path=recognized_images_file_path,
                                  non_recognized_images_file_path=non_recognized_images_file_path)
    start_alpr.create_stop_flag()
    results_generator = start_alpr.start_service()
