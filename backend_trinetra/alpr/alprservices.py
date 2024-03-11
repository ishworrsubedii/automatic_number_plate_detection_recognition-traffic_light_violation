import time
import re
import os
import threading
from django.utils import timezone
from .models import ImageCaptureDatabase, ImageLoadDatabase, ALPRRecognizedImageDatabase, \
    ALPRNonRecognizedImageDatabase, ALPRDatabase, ALPRecognitionDatabase
from services.alpr.usage.start.start_image_capture import StartImageCaptureExample
from services.alpr.usage.stop.stop_image_capture import StopImageCaptureExample
from services.alpr.usage.start.start_image_load import StartImageLoadExample
from services.alpr.usage.stop.stop_image_load import update_file
from services.alpr.usage.start.start_alpr import StartAlprExample
from services.alpr.usage.stop.stop_alpr import StopAlprExample


class ALPRServices:
    def __init__(self):
        self.CAPTURE_FLAG_PATH = "services/alpr/resources/flag_check/capture_status.txt"
        self.LOAD_FLAG_PATH = "services/alpr/resources/flag_check/start_load_status.txt"
        self.RECOGNITION_FLAG_PATH = "services/alpr/resources/flag_check/alpr_status.txt"
        self.IMAGE_DIR = 'services/alpr/resources/rtsp/'
        self.DET_MODEL = 'services/alpr/resources/paddleocr/Multilingual_PP-OCRv3_det_infer/'
        self.RECOG_MODEL = 'services/alpr/resources/paddleocr/mar-8'
        self.CHAR_DICT = 'services/alpr/resources/paddleocr/mar-8/devanagari_dict.txt'
        self.OUTPUT_PATH = 'services/alpr/output/paddleocr_rec_output/'
        self.NON_REC_OUTPUT_PATH = 'services/alpr/output/paddleocr_non_rec_output/'
        self.THRESHOLD = 3
        self.SOURCE = 'rtsp://ishwor:subedi@192.168.1.106:5555/h264_opus.sdp'
        self.MODEL_PATH = 'services/alpr/resources/yolov8/nnpd.pt'
        self.CAPTURED_IMAGE_SAVE_DIR = 'services/alpr/resources/rtsp/'
        self.DETECTED_IMAGE_SAVE_DIR = 'services/alpr/resources/plate_detected/'
        self.RESULT_SAVE_PATH = "services/alpr/output/result.txt"
        self.RECOGNIZED_IMAGES_FILE_PATH = "services/alpr/output/recognized_images_paths.txt"
        self.NON_RECOGNIZED_IMAGES_FILE_PATH = "services/alpr/output/non_recognized_images_paths.txt"
        self.FONT_PATH = 'services/alpr/resources/fonts/nepali.ttf'

    def start_image_capture(self):
        image_capture_database = ImageCaptureDatabase(status='in_progress')
        image_capture_database.save()
        image_capture_service = StartImageCaptureExample(
            self.CAPTURE_FLAG_PATH, self.SOURCE, self.CAPTURED_IMAGE_SAVE_DIR, self.THRESHOLD
        )
        image_capture_service.create_stop_flag()
        image_capture_service.start_service()

    def stop_image_capture(self):
        image_capture_database = ImageCaptureDatabase.objects.latest('id')
        image_capture_database.stopped_at = timezone.now()
        image_capture_database.status = 'stopped'
        image_capture_database.save()
        stop_service = StopImageCaptureExample(self.CAPTURE_FLAG_PATH)
        stop_service.stop_image_capture_service()

    def start_load_image(self):
        image_load_database = ImageLoadDatabase(status='in_progress')
        image_load_database.save()
        image_load_service = StartImageLoadExample(
            self.LOAD_FLAG_PATH, self.IMAGE_DIR, self.MODEL_PATH, self.DETECTED_IMAGE_SAVE_DIR
        )
        image_load_service.create_stop_flag()
        image_load_service.start_service()

    def stop_load_image(self):
        image_load_database = ImageLoadDatabase.objects.latest('id')
        image_load_database.stopped_at = timezone.now()
        image_load_database.status = 'stopped'
        image_load_database.save()
        update_file(self.LOAD_FLAG_PATH)

    def save_recognized_image(self):
        while True:
            with open(self.RECOGNIZED_IMAGES_FILE_PATH, 'r+') as recognized_images_file:
                lines = recognized_images_file.readlines()
                if lines:
                    line = lines[0]
                    recognized_image_path_line = re.search(r'Recognized_image_path:(.*)', line)
                    if recognized_image_path_line:
                        recognized_image_path = recognized_image_path_line.group(1).strip()
                        recognized_alpr_images_list = ALPRRecognizedImageDatabase()
                        recognized_alpr_images_list.recognized_image_path = recognized_image_path
                        try:
                            pass
                            recognized_alpr_images_list.save()
                        except Exception as e:
                            print(f"Error saving recognized image: {e}")

                    del lines[0]
                    time.sleep(2)
                    recognized_images_file.seek(0)
                    recognized_images_file.truncate()
                    recognized_images_file.writelines(lines)

    def save_non_recognized_image(self):
        while True:
            with open(self.NON_RECOGNIZED_IMAGES_FILE_PATH, 'r+') as non_recognized_images_file:
                lines = non_recognized_images_file.readlines()
                if lines:
                    line = lines[0]
                    non_recognized_image_path_line = re.search(r'Non_Recognized_image_path:(.*)', line)

                    if non_recognized_image_path_line:
                        non_recognized_image_path = non_recognized_image_path_line.group(1).strip()
                        non_recognized_alpr_images_list = ALPRNonRecognizedImageDatabase()
                        non_recognized_alpr_images_list.non_recognized_image_path = non_recognized_image_path
                        try:
                            non_recognized_alpr_images_list.save()
                            pass
                        except Exception as e:
                            print(f"Error saving non recognized image: {e}")

                    del lines[0]
                    time.sleep(2)
                    non_recognized_images_file.seek(0)
                    non_recognized_images_file.truncate()
                    non_recognized_images_file.writelines(lines)

    def save_recognition_info(self):
        while True:
            with open(self.RESULT_SAVE_PATH, 'r+') as result_file:
                lines = result_file.readlines()
                if lines:
                    line = lines[0]
                    image_path_match = re.search(r'Image_path:(.*?),', line)
                    text_match = re.search(r'Text: (.*?),', line)
                    score_match = re.search(r'Score: (.*?),', line)
                    date_match = re.search(r'Date_recognized:(.*)$', line)
                    if image_path_match and text_match and score_match and date_match:
                        recognized_info_database = ALPRecognitionDatabase()
                        recognized_info_database.detection_id = 'ALPR' + date_match.group(1)[:4]
                        recognized_info_database.image_path = image_path_match.group(1).strip()
                        recognized_info_database.recognized_info = text_match.group(1).strip()
                        recognized_info_database.accuracy = score_match.group(1).strip()
                        recognized_info_database.date = date_match.group(1).strip()
                        recognized_info_database.status = 'done'
                        try:
                            recognized_info_database.save()

                        except Exception as e:
                            print(f"Error saving recognition info: {e}")

                    del lines[0]
                    time.sleep(2)
                    result_file.seek(0)
                    result_file.truncate()
                    result_file.writelines(lines)

    def start_recognize_plate_for_thread(self):
        try:
            alpr_database = ALPRDatabase(status='in_progress')
            alpr_database.save()
        except Exception as e:
            print(f"Error saving ALPRDatabase: {e}")
        start_alpr = StartAlprExample(
            det_model=self.DET_MODEL, recognition_model=self.RECOG_MODEL, rec_char_dict=self.CHAR_DICT,
            detected_img_dir=self.DETECTED_IMAGE_SAVE_DIR,
            output_path=self.OUTPUT_PATH, non_rec_output_path=self.NON_REC_OUTPUT_PATH,
            flag_path=self.RECOGNITION_FLAG_PATH, result_file=self.RESULT_SAVE_PATH,
            recognized_images_file_path=self.RECOGNIZED_IMAGES_FILE_PATH,
            non_recognized_images_file_path=self.NON_RECOGNIZED_IMAGES_FILE_PATH,

            font_path=self.FONT_PATH
        )
        start_alpr.create_stop_flag()
        start_alpr.start_service()

    def start_recognize_plate(self):
        try:
            self.database_save_thread = threading.Thread(target=self.save_recognition_info)
            self.alpr_service_thread = threading.Thread(target=self.start_recognize_plate_for_thread)
            self.database_save_image_recognized_path = threading.Thread(target=self.save_recognized_image)
            self.database_save_image_non_recognized_path = threading.Thread(target=self.save_non_recognized_image)

            self.database_save_thread.start()
            self.alpr_service_thread.start()
            self.database_save_image_recognized_path.start()
            self.database_save_image_non_recognized_path.start()
        except Exception as e:
            print(f"Error starting ALPR services: {e}")
        finally:
            self.database_save_thread.join()
            self.alpr_service_thread.join()
            self.database_save_image_recognized_path.join()
            self.database_save_image_non_recognized_path.join()

    def stop_recognize_plate(self):
        alpr_database = ALPRDatabase.objects.latest('id')
        alpr_database.stopped_at = timezone.now()
        alpr_database.status = 'stopped'
        alpr_database.save()
        stop_service = StopAlprExample(self.RECOGNITION_FLAG_PATH)
        stop_service.stop_anpr_service()

        self.database_save_thread.join()
        self.alpr_service_thread.join()
        self.database_save_image_recognized_path.join()
        self.database_save_image_non_recognized_path.join()
