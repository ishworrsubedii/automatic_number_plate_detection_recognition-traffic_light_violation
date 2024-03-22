"""
Created By: ishwor subedi
Date: 2024-02-28
"""
import threading
import time
import re
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

from .models import ALPRRecognitionResultDatabaseTrafficLight, ALPRRecognizedImageDatabaseTrafficLight, \
    ALPRNonRecognizedImageDatabaseTrafficLight, ImageCaptureDatabaseTrafficLight, NumberPlateRecognitionTrafficLight, \
    NumberPlateDetectionTrafficLight, VehicleDetectionTrafficLight, RedLightViolatedVehiclesListTrafficLight, \
    VehicleNotDetectedImageListDatabaseTrafficLight, TrafficlightColorDetectionTrafficlight


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
        self.RED_LIGHT_DETECTED_IMAGE_FILE_TXT = "services/trafficlight/output/vehicle_detection/detected_images_path.txt"
        self.RED_LIGHT_NON_DETECTED_IMAGE_FILE_TXT = "services/trafficlight/output/vehicle_detection/non_detected_images_path.txt"
        # Number plate detection
        self.NUMBER_PLATE_DETECTION_FLAG = "services/trafficlight/resources/flag_check/number_plate_status"
        self.NUMBER_PLATE_DETECTION_MODEL_PATH = 'services/alpr/resources/yolov8/nnpd.pt'
        self.NUMBER_PLATE_DETECTED_IMAGE_SAVE_DIR = 'services/trafficlight/resources/plate_detected'
        # Automatic number plate recognition
        self.ANPR_DET_MODEL_PATH = 'services/trafficlight/resources/paddleocr/Multilingual_PP-OCRv3_det_infer'
        self.ANPR_REC_MODEL_PATH = 'services/alpr/resources/paddleocr/mar-18'
        self.REC_CHAR_DIR = 'services/alpr/resources/paddleocr/mar-8/devanagari_dict.txt'

        self.RECOGNIZED_OUTPUT_DIR_PATH = 'services/trafficlight/output/paddleocr_output/paddleocr_rec_output'
        self.NON_RECOGNIZED_OUTPUT_DIR_PATH = "services/trafficlight/output/paddleocr_output/paddleocr_non_rec_output"
        self.ANPR_FONT_PATH = 'services/trafficlight/resources/paddleocr/fonts/nepali.ttf'
        self.ANPR_FLAG_PATH = 'services/trafficlight/resources/flag_check/alpr_status'

        self.ANPR_RESULT_PATH = "services/trafficlight/output/paddleocr_output/result.txt"
        self.ANPR_RECOGNIZED_IMAGES_FILE_NAME_TXT = "services/trafficlight/output/paddleocr_output/recognized_images_paths.txt"
        self.ANPR_NON_RECOGNIZED_IMAGES_FILE_NAME_TXT = "services/trafficlight/output/paddleocr_output/non_recognized_images_paths.txt"

        self.draw_polygon = True

        self.save_recognition_info_traffic_light = None
        self.start_recognition_info_traffic_light = None
        self.save_recognition_images_traffic_light = None
        self.save_non_recognition_images_traffic_light = None
        self.traffic_light_violated_image_save = None
        self.vehicle_non_detected_inside_polygon_save = None
        self.vehicle_detection_polygon_services_thread = None

        self.start_recognize_plate_thread_running = False
        self.vehicle_detection_polygon_image_path_save_thread = False

    def start_image_capture_traffic_light(self):
        image_capture_database_traffic_violation = ImageCaptureDatabaseTrafficLight(status="in_progress")
        image_capture_database_traffic_violation.save()
        image_capture_service = StartImageCaptureTrafficLight(self.CAPTURE_FLAG_PATH, self.SOURCE,
                                                              self.IMAGE_PATH_TO_SAVE,
                                                              self.IMAGE_HASH_THRESHOLD)
        image_capture_service.create_stop_flag()
        image_capture_service.start_service()

    def stop_image_capture_traffic_light(self):
        image_capture_database_traffic_violation = ImageCaptureDatabaseTrafficLight.objects.latest('id')
        image_capture_database_traffic_violation.stopped_at = timezone.now()
        image_capture_database_traffic_violation.status = "stopped"
        image_capture_database_traffic_violation.save()
        stop_service = StopImageCaptureTrafficLight(self.CAPTURE_FLAG_PATH)
        stop_service.stop_image_capture_service()

    def start_traffic_light_color_detection(self):
        color_traffic_light_detection_traffic_violation = TrafficlightColorDetectionTrafficlight(status="in_progress")
        color_traffic_light_detection_traffic_violation.save()
        start_traffic_light_color_detection = StartTrafficLightColorDetectionExample(template_paths=self.TEMPLATE_PATHS,
                                                                                     image_directory=self.IMAGE_PATH_TO_SAVE,
                                                                                     display=self.TRAFFIC_LIGHT_DISPLAY,
                                                                                     flag_path=self.TRAFFIC_LIGHT_FLAG_PATH,
                                                                                     red_light_detected=self.RED_LIGHT_DETECTED
                                                                                     )
        start_traffic_light_color_detection.create_stop_flag()
        start_traffic_light_color_detection.start_service()

    def stop_traffic_light_color_detection(self):
        color_traffic_light_detection_traffic_violation = TrafficlightColorDetectionTrafficlight.objects.latest('id')
        color_traffic_light_detection_traffic_violation.stopped_at = timezone.now()
        color_traffic_light_detection_traffic_violation.status = "stopped"
        color_traffic_light_detection_traffic_violation.save()
        stop_traffic_color_light_detection(self.TRAFFIC_LIGHT_FLAG_PATH)

    def vehicle_detection_polygon(self):
        vehicle_detection_traffic_violation = VehicleDetectionTrafficLight(status="in_progress")
        vehicle_detection_traffic_violation.save()
        vehicle_detector_server = StartVehicleDetectionExample(
            flag_path=self.VEHICLE_DETECTION_FLAG_PATH,
            polygon_points=self.POLYGON_POINTS,
            model_path=self.VEHICLE_DETECTION_MODEL_PATH,
            detected_images=self.VEHICLE_DETECTED_IMAGE_DIR,
            non_detected_images=self.VEHICLE_NON_DETECTED_IMAGE_DIR,
            red_light_detected=self.RED_LIGHT_DETECTED,
            display=self.VEHICLE_DETECTION_DISPLAY,
            red_light_vehicle_detected_path=self.RED_LIGHT_DETECTED_IMAGE_FILE_TXT,
            red_light_vehicle_non_detected_path=self.RED_LIGHT_NON_DETECTED_IMAGE_FILE_TXT,
            draw_polygon=self.draw_polygon

        )
        vehicle_detector_server.create_stop_flag()
        vehicle_detector_server.start_service()

    def start_vehicle_detection_polygon(self):
        try:
            self.vehicle_detection_polygon_image_path_save_thread = True
            self.vehicle_detection_polygon_services_thread = threading.Thread(target=self.vehicle_detection_polygon)
            self.traffic_light_violated_image_save = threading.Thread(target=self.save_vehicle_detected_image)
            self.vehicle_non_detected_inside_polygon_save = threading.Thread(
                target=self.save_vehicle_non_detected_image)

            self.vehicle_detection_polygon_services_thread.start()
            self.traffic_light_violated_image_save.start()
            self.vehicle_non_detected_inside_polygon_save.start()
        except Exception as e:
            print(f"Error starting vehicle detection services: {e}")
        finally:
            self.vehicle_detection_polygon_services_thread.join()
            self.traffic_light_violated_image_save.join()
            self.vehicle_non_detected_inside_polygon_save.join()

    def stop_vehicle_detection_polygon(self):
        vehicle_detection_traffic_violation = VehicleDetectionTrafficLight.objects.latest('id')
        vehicle_detection_traffic_violation.stopped_at = timezone.now()
        vehicle_detection_traffic_violation.status = "stopped"
        vehicle_detection_traffic_violation.save()
        stop_vehicle_detection(self.VEHICLE_DETECTION_FLAG_PATH)
        if self.vehicle_detection_polygon_image_path_save_thread:
            self.traffic_light_violated_image_save.join()
            self.vehicle_non_detected_inside_polygon_save.join()

    def start_number_plate_detection(self):
        number_plate_detection_traffic_violation = NumberPlateDetectionTrafficLight(status="in_progress")
        number_plate_detection_traffic_violation.save()
        image_load_service = StartImageLoadExample(flag_path=self.NUMBER_PLATE_DETECTION_FLAG,
                                                   image_dir=self.VEHICLE_DETECTED_IMAGE_DIR,
                                                   model_path=self.NUMBER_PLATE_DETECTION_MODEL_PATH,
                                                   image_save_dir=self.NUMBER_PLATE_DETECTED_IMAGE_SAVE_DIR)
        image_load_service.create_stop_flag()
        image_load_service.start_service()
        time.sleep(1)

    def stop_number_plate_detection(self):
        number_plate_detection_traffic_violation = NumberPlateDetectionTrafficLight.objects.latest('id')
        number_plate_detection_traffic_violation.stopped_at = timezone.now()
        number_plate_detection_traffic_violation.status = "stopped"
        number_plate_detection_traffic_violation.save()
        stop_number_plate_detection(self.NUMBER_PLATE_DETECTION_FLAG)

    def save_vehicle_detected_image(self):
        while True:
            with open(self.RED_LIGHT_DETECTED_IMAGE_FILE_TXT, 'r+') as recognized_images_file:
                lines = recognized_images_file.readlines()
                if lines:
                    line = lines[0]
                    detected_image_path_line = re.search(r'Detected_image_path:(.*)', line)
                    if detected_image_path_line:
                        red_light_violated_vehicles = detected_image_path_line.group(1).strip()
                        traffic_light_violated_img = RedLightViolatedVehiclesListTrafficLight()
                        traffic_light_violated_img.traffic_light_violated_images = red_light_violated_vehicles
                        try:
                            pass
                            traffic_light_violated_img.save()
                        except Exception as e:
                            print(f"Error saving recognized image: {e}")

                    del lines[0]
                    recognized_images_file.seek(0)
                    recognized_images_file.truncate()
                    recognized_images_file.writelines(lines)

    def save_vehicle_non_detected_image(self):
        while True:
            with open(self.RED_LIGHT_NON_DETECTED_IMAGE_FILE_TXT, 'r+') as non_recognized_images_file:
                lines = non_recognized_images_file.readlines()
                if lines:
                    line = lines[0]
                    non_detected_image_path_line = re.search(r'Non_detected_image_path:(.*)', line)

                    if non_detected_image_path_line:
                        non_recognized_image_path = non_detected_image_path_line.group(1).strip()
                        non_detected_vehicle_images_list = VehicleNotDetectedImageListDatabaseTrafficLight()
                        non_detected_vehicle_images_list.vehicle_not_detected_images = non_recognized_image_path
                        try:
                            non_detected_vehicle_images_list.save()
                            pass
                        except Exception as e:
                            print(f"Error saving non recognized image: {e}")

                    del lines[0]
                    non_recognized_images_file.seek(0)
                    non_recognized_images_file.truncate()
                    non_recognized_images_file.writelines(lines)

    def save_recognized_image(self):
        while True:
            with open(self.ANPR_RECOGNIZED_IMAGES_FILE_NAME_TXT, 'r+') as recognized_images_file:
                lines = recognized_images_file.readlines()
                if lines:
                    line = lines[0]
                    recognized_image_path_line = re.search(r'Recognized_image_path:(.*)', line)
                    if recognized_image_path_line:
                        recognized_image_path = recognized_image_path_line.group(1).strip()
                        recognized_alpr_images_list = ALPRRecognizedImageDatabaseTrafficLight()
                        recognized_alpr_images_list.recognized_image_path = recognized_image_path
                        try:
                            pass
                            recognized_alpr_images_list.save()
                        except Exception as e:
                            print(f"Error saving recognized image: {e}")

                    del lines[0]
                    recognized_images_file.seek(0)
                    recognized_images_file.truncate()
                    recognized_images_file.writelines(lines)

    def save_non_recognized_image(self):
        while True:
            with open(self.ANPR_NON_RECOGNIZED_IMAGES_FILE_NAME_TXT, 'r+') as non_recognized_images_file:
                lines = non_recognized_images_file.readlines()
                if lines:
                    line = lines[0]
                    non_recognized_image_path_line = re.search(r'Non_Recognized_image_path:(.*)', line)

                    if non_recognized_image_path_line:
                        non_recognized_image_path = non_recognized_image_path_line.group(1).strip()
                        non_recognized_alpr_images_list = ALPRNonRecognizedImageDatabaseTrafficLight()
                        non_recognized_alpr_images_list.non_recognized_image_path = non_recognized_image_path
                        try:
                            non_recognized_alpr_images_list.save()
                            pass
                        except Exception as e:
                            print(f"Error saving non recognized image: {e}")

                    del lines[0]
                    non_recognized_images_file.seek(0)
                    non_recognized_images_file.truncate()
                    non_recognized_images_file.writelines(lines)

    def save_recognition_info(self):
        while True:
            with open(self.ANPR_RESULT_PATH, 'r+') as result_file:
                lines = result_file.readlines()
                if lines:
                    line = lines[0]
                    image_path_match = re.search(r'Image_path:(.*?),', line)
                    text_match = re.search(r'Text: (.*?),', line)
                    score_match = re.search(r'Score: (.*?),', line)
                    date_match = re.search(r'Date_recognized:(.*)$', line)
                    if image_path_match and text_match and score_match and date_match:
                        recognized_info_database = ALPRRecognitionResultDatabaseTrafficLight()
                        recognized_info_database.violation_id = 'TFF-ALPR' + date_match.group(1)[:4]
                        recognized_info_database.image_path = image_path_match.group(1).strip()
                        recognized_info_database.recognized_info = text_match.group(1).strip()
                        recognized_info_database.accuracy = score_match.group(1).strip()
                        recognized_info_database.date = date_match.group(1).strip()
                        recognized_info_database.violation_type = 'Traffic Light Violation'
                        recognized_info_database.status = 'done'
                        try:
                            recognized_info_database.save()

                        except Exception as e:
                            print(f"Error saving recognition info: {e}")

                    del lines[0]
                    result_file.seek(0)
                    result_file.truncate()
                    result_file.writelines(lines)

    def automatic_number_plate_recognition(self):
        try:
            alpr_recognition_traffic_violation = NumberPlateRecognitionTrafficLight(status="in_progress")
            alpr_recognition_traffic_violation.save()
        except Exception as e:
            print(f"Error saving alpr recognition status: {e}")

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

    def start_automatic_number_plate_recognition(self):
        try:
            self.start_recognize_plate_thread_running = True
            self.save_recognition_info_traffic_light = threading.Thread(target=self.save_recognition_info)
            self.start_recognition_info_traffic_light = threading.Thread(
                target=self.automatic_number_plate_recognition)
            self.save_recognition_images_traffic_light = threading.Thread(target=self.save_recognized_image)
            self.save_non_recognition_images_traffic_light = threading.Thread(target=self.save_non_recognized_image)

            self.save_recognition_info_traffic_light.start()
            self.start_recognition_info_traffic_light.start()
            self.save_recognition_images_traffic_light.start()
            self.save_non_recognition_images_traffic_light.start()
        except Exception as e:
            print(f"Error starting ALPR services: {e}")
        finally:
            self.save_recognition_info_traffic_light.join()
            self.start_recognition_info_traffic_light.join()
            self.save_recognition_images_traffic_light.join()
            self.save_non_recognition_images_traffic_light.join()

    def stop_automatic_number_plate_recognition(self):
        alpr_recognition_traffic_violation = NumberPlateRecognitionTrafficLight.objects.latest('id')
        alpr_recognition_traffic_violation.stopped_at = timezone.now()
        alpr_recognition_traffic_violation.status = "stopped"
        alpr_recognition_traffic_violation.save()
        stop_service = StopAlprExample(self.ANPR_FLAG_PATH)
        stop_service.stop_anpr_service()
        if self.start_recognize_plate_thread_running:
            self.start_recognize_plate_thread_running = False

            self.save_recognition_info_traffic_light.join()
            self.start_recognition_info_traffic_light.join()

            self.save_recognition_images_traffic_light.join()
            self.save_non_recognition_images_traffic_light.join()
