"""
Created By: ishwor subedi
Date: 2024-02-28
"""
import time
import re
import os
from django.utils import timezone
import numpy as np
from services.trafficlight.usages.start.start_image_capture_traffic_light import StartImageCaptureTrafficLight

from services.trafficlight.usages.start.start_traffic_color_detection_save import \
    StartTrafficLightColorDetectionExample
from services.trafficlight.usages.start.start_vehicle_detection import StartVehicleDetectionExample
from services.trafficlight.usages.stop.stop_alpr import StopAlprExample
from services.trafficlight.usages.stop.stop_image_capture_traffic_light import StopImageCaptureTrafficLight
from services.trafficlight.usages.stop.stop_number_plate_detection import stop_number_plate_detection
from services.trafficlight.usages.stop.stop_traffic_color_light_detection import \
    stop_traffic_color_light_detection
from services.trafficlight.usages.stop.stop_vehicle_detection import stop_vehicle_detection
from services.trafficlight.usages.start.start_number_plate_det import StartImageLoadExample
from services.trafficlight.usages.start.start_alpr import StartAlprExample


class TrafficLightViolationService:
    def __init__(self):
        # image capture
        self.CAPTURE_FLAG_PATH = "services/trafficlight/resources/flag_check/capture.txt"
        self.SOURCE = '/home/ishwor/Desktop/dataset/vehicle/video/traffic/VID20240222103234.mp4'
        self.IMAGE_PATH_TO_SAVE = "services/trafficlight/resources/rtsp/"
        self.IMAGE_HASH_THRESHOLD = 0

        # traffic light color detection
        self.TEMPLATE_PATHS = ['services/trafficlight/resources/template_images/template1.png',
                               'services/trafficlight/resources/template_images/template2.png',
                               'services/trafficlight/resources/template_images/template3.png']
        self.RED_LIGHT_DETECTED = "services/trafficlight/resources/red_light_detected"

        self.TRAFFIC_LIGHT_DISPLAY = True
        self.TRAFFIC_LIGHT_FLAG_PATH = 'services/trafficlight/resources/flag_check/traffic_light.txt'

        # Vehicle detection
        self.VEHICLE_DETECTION_FLAG_PATH = "services/trafficlight/resources/flag_check/vehicle_det.txt"
        self.POLYGON_POINTS = np.array([(615, 340), (909, 346), (1006, 437), (631, 461)])
        self.VEHICLE_DETECTION_MODEL_PATH = "services/trafficlight/resources/vehicle_detection/yolov8n.pt"
        self.VEHICLE_DETECTED_IMAGE_DIR = "services/trafficlight/output/vehicle_detection/detected"
        self.VEHICLE_NON_DETECTED_IMAGE_DIR = "services/trafficlight/output/vehicle_detection/non_detected"
        self.VEHICLE_DETECTION_DISPLAY = False
        self.RED_LIGHT_DETECTED_IMAGE_FILE_TXT = "services/trafficlight/output/vehicle_detection/detected_images_path"
        self.RED_LIGHT_NON_DETECTED_IMAGE_FILE_TXT = "services/trafficlight/output/vehicle_detection/non_detected_images_path"
        # Number plate detection
        self.NUMBER_PLATE_DETECTION_FLAG = "services/trafficlight/resources/flag_check/number_plate_status"
        self.NUMBER_PLATE_DETECTION_MODEL_PATH = 'services/alpr/resources/yolov8/nnpd.pt'
        self.NUMBER_PLATE_DETECTED_IMAGE_SAVE_DIR = 'services/trafficlight/resources/plate_detected'
        # Automatic number plate recognition
        self.ANPR_DET_MODEL_PATH = 'services/trafficlight/resources/paddleocr/Multilingual_PP-OCRv3_det_infer'
        self.ANPR_REC_MODEL_PATH = 'services/trafficlight/resources/paddleocr/custom_rec'
        self.REC_CHAR_DIR = 'services/trafficlight/resources/paddleocr/devanagari_dict.txt'

        self.RECOGNIZED_OUTPUT_DIR_PATH = 'services/trafficlight/output/paddleocr_output/paddleocr_rec_output'
        self.NON_RECOGNIZED_OUTPUT_DIR_PATH = "services/trafficlight/output/paddleocr_output/paddleocr_non_rec_output"
        self.ANPR_FONT_PATH = 'services/trafficlight/resources/paddleocr/fonts/nepali.ttf'
        self.ANPR_FLAG_PATH = 'services/trafficlight/resources/flag_check/alpr_status'

        self.ANPR_RESULT_PATH = "services/trafficlight/output/paddleocr_output/result.txt"
        self.ANPR_RECOGNIZED_IMAGES_FILE_NAME_TXT = "services/trafficlight/output/paddleocr_output/recognized_images_paths.txt"
        self.ANPR_NON_RECOGNIZED_IMAGES_FILE_NAME_TXT = "services/trafficlight/output/paddleocr_output/non_recognized_images_paths.txt"

    def start_image_capture_traffic_light(self):
        image_capture_service = StartImageCaptureTrafficLight(self.CAPTURE_FLAG_PATH, self.SOURCE,
                                                              self.IMAGE_PATH_TO_SAVE,
                                                              self.IMAGE_HASH_THRESHOLD)
        image_capture_service.create_stop_flag()
        image_capture_service.start_service()
        time.sleep(1)

    def stop_image_capture_traffic_light(self):
        stop_service = StopImageCaptureTrafficLight(self.CAPTURE_FLAG_PATH)
        stop_service.stop_image_capture_service()

    def start_traffic_light_color_detection(self):
        start_traffic_light_color_detection = StartTrafficLightColorDetectionExample(template_paths=self.TEMPLATE_PATHS,
                                                                                     image_directory=self.IMAGE_PATH_TO_SAVE,
                                                                                     display=self.TRAFFIC_LIGHT_DISPLAY,
                                                                                     flag_path=self.TRAFFIC_LIGHT_FLAG_PATH,
                                                                                     red_light_detected=self.RED_LIGHT_DETECTED
                                                                                     )
        start_traffic_light_color_detection.create_stop_flag()
        start_traffic_light_color_detection.start_service()

    def stop_traffic_light_color_detection(self):
        stop_traffic_color_light_detection(self.TRAFFIC_LIGHT_FLAG_PATH)

    def start_vehicle_detection_polygon(self):
        vehicle_detector_server = StartVehicleDetectionExample(
            flag_path=self.VEHICLE_DETECTION_FLAG_PATH,
            polygon_points=self.POLYGON_POINTS,
            model_path=self.VEHICLE_DETECTION_MODEL_PATH,
            detected_images=self.VEHICLE_DETECTED_IMAGE_DIR,
            non_detected_images=self.VEHICLE_NON_DETECTED_IMAGE_DIR,
            red_light_detected=self.RED_LIGHT_DETECTED,
            display=self.VEHICLE_DETECTION_DISPLAY,
            red_light_vehicle_detected_path=self.RED_LIGHT_DETECTED_IMAGE_FILE_TXT,
            red_light_vehicle_non_detected_path=self.RED_LIGHT_NON_DETECTED_IMAGE_FILE_TXT

        )
        vehicle_detector_server.create_stop_flag()
        vehicle_detector_server.start_service()

    def stop_vehicle_detection_polygon(self):
        stop_vehicle_detection(self.VEHICLE_DETECTION_FLAG_PATH)

    def start_number_plate_detection(self):
        image_load_service = StartImageLoadExample(flag_path=self.NUMBER_PLATE_DETECTION_FLAG,
                                                   image_dir=self.VEHICLE_DETECTED_IMAGE_DIR,
                                                   model_path=self.NUMBER_PLATE_DETECTION_MODEL_PATH,
                                                   image_save_dir=self.NUMBER_PLATE_DETECTED_IMAGE_SAVE_DIR)
        image_load_service.create_stop_flag()
        image_load_service.start_service()
        time.sleep(1)

    def stop_number_plate_detection(self):
        stop_number_plate_detection(self.NUMBER_PLATE_DETECTION_FLAG)

    def start_automatic_number_plate_recognition(self):
        start_alpr = StartAlprExample(det_model=self.ANPR_DET_MODEL_PATH, recognition_model=self.ANPR_REC_MODEL_PATH,
                                      rec_char_dict=self.REC_CHAR_DIR,
                                      detected_img_dir=self.NUMBER_PLATE_DETECTED_IMAGE_SAVE_DIR,
                                      output_path=self.RECOGNIZED_OUTPUT_DIR_PATH,
                                      non_rec_output_path=self.NON_RECOGNIZED_OUTPUT_DIR_PATH,
                                      flag_path=self.ANPR_FLAG_PATH
                                      , result_file=self.ANPR_RESULT_PATH,
                                      recognized_images_file_path=self.ANPR_RECOGNIZED_IMAGES_FILE_NAME_TXT,
                                      non_recognized_images_file_path=self.ANPR_NON_RECOGNIZED_IMAGES_FILE_NAME_TXT,
                                      font_path=self.ANPR_FONT_PATH
                                      )
        start_alpr.create_stop_flag()
        start_alpr.start_service()

    def stop_automatic_number_plate_recognition(self):
        stop_service = StopAlprExample(self.ANPR_FLAG_PATH)
        stop_service.stop_anpr_service()
