import time
from datetime import datetime

from django.utils import timezone
from services.alpr.usage.start.start_image_capture import StartImageCaptureExample
from services.alpr.usage.stop.stop_image_capture import StopImageCaptureExample
from services.alpr.usage.start.start_image_load import StartImageLoadExample
from services.alpr.usage.stop.stop_image_load import update_file
from services.alpr.usage.start.start_alpr import StartAlprExample
from services.alpr.usage.stop.stop_alpr import StopAlprExample

from .models import ImageCaptureDatabase, ImageLoadDatabase, ALPRDatabase, ALPRecognitionDatabase


class ALPRServices:
    def __init__(self):
        self.CAPTURE_FLAG_PATH = "services_trinetra/alpr/resources/flag_check/capture_status.txt"
        self.LOAD_FLAG_PATH = "services_trinetra/alpr/resources/flag_check/start_load_status.txt"
        self.RECOGNITION_FLAG_PATH = "services_trinetra/alpr/resources/flag_check/alpr_status.txt"
        self.IMAGE_DIR = 'services_trinetra/alpr/resources/rtsp/'
        self.DET_MODEL = 'services_trinetra/alpr/resources/paddleocr/Multilingual_PP-OCRv3_det_infer/'
        self.RECOG_MODEL = 'services_trinetra/alpr/resources/paddleocr/custom_recog/'
        self.CHAR_DICT = 'services_trinetra/alpr/resources/paddleocr/devanagari_dict.txt'
        self.OUTPUT_PATH = 'services_trinetra/alpr/output/paddleocr_rec_output/'
        self.FONT_PATH = 'services_trinetra/alpr/resources/fonts/nepali.ttf'
        self.THRESHOLD = 5
        self.SOURCE = 'rtsp://ishwor:subedi@192.168.1.106:5555/h264_opus.sdp'
        self.MODEL_PATH = 'services_trinetra/alpr/resources/yolov8/nnpd.pt'
        self.IMAGE_SAVE_DIR = 'services_trinetra/alpr/resources/plate_detected/'

    def start_image_capture(self):
        image_capture_service = StartImageCaptureExample(
            self.CAPTURE_FLAG_PATH, self.SOURCE, self.IMAGE_SAVE_DIR, self.THRESHOLD
        )
        image_capture_service.create_stop_flag()
        image_capture_service.start_service()
        time.sleep(1)

        image_capture_database = ImageCaptureDatabase(status='in_progress')
        image_capture_database.save()

    def stop_image_capture(self):
        stop_service = StopImageCaptureExample(self.CAPTURE_FLAG_PATH)
        stop_service.stop_image_capture_service()

        image_capture_database = ImageCaptureDatabase.objects.latest('id')
        image_capture_database.stopped_at = timezone.now()
        image_capture_database.status = 'stopped'
        image_capture_database.save()

    def start_load_image(self):
        image_load_service = StartImageLoadExample(
            self.LOAD_FLAG_PATH, self.IMAGE_DIR, self.MODEL_PATH, self.IMAGE_SAVE_DIR
        )
        image_load_service.create_stop_flag()
        image_load_service.start_service()
        time.sleep(1)

        image_load_database = ImageLoadDatabase(status='in_progress')
        image_load_database.save()

    def stop_load_image(self):
        update_file(self.LOAD_FLAG_PATH)
        image_load_database = ImageLoadDatabase.objects.latest('id')
        image_load_database.stopped_at = timezone.now()
        image_load_database.status = 'stopped'
        image_load_database.save()

    def start_recognize_plate(self):
        start_alpr = StartAlprExample(
            self.DET_MODEL, self.RECOG_MODEL, self.CHAR_DICT, self.IMAGE_SAVE_DIR,
            self.OUTPUT_PATH, self.RECOGNITION_FLAG_PATH
        )
        start_alpr.create_stop_flag()
        results_generator = start_alpr.main_alpr_service(self.IMAGE_SAVE_DIR)

        detection_id_counter = 1  # Initialize the counter

        for boxes, txts, scores in results_generator:
            detection_id = f"DTALPR{detection_id_counter}"  # Create detection_id
            alprecog_database = ALPRecognitionDatabase(
                detection_id=detection_id,
                recognized_info=txts,
                accuracy=scores,
                status='in_progress'
            )
            alprecog_database.save()

            detection_id_counter += 1  #

        alpr_database = ALPRDatabase(status='in_progress')
        alpr_database.save()


def stop_recognize_plate(self):
    stop_service = StopAlprExample(self.RECOGNITION_FLAG_PATH)
    stop_service.stop_anpr_service()

    alpr_database = ALPRDatabase.objects.latest('id')
    alpr_database.stopped_at = timezone.now()
    alpr_database.status = 'stopped'
    alpr_database.save()
