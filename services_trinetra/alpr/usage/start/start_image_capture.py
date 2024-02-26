import os
import time

from services.alpr.src.services.detection.image_capture import CaptureMain
from services.alpr.usage import image_capture_logger

IMAGE_CAPTURE_LOGGER = image_capture_logger()


class StartImageCaptureExample:
    def __init__(self, flag_path, source, image_path_to_save, image_hash_threshold):
        self.flag_path = flag_path
        self.source = source
        self.image_path_to_save = image_path_to_save
        self.image_hash_threshold = image_hash_threshold
        self.running = False

    def create_stop_flag(self):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write('False')
        except Exception as e:
            IMAGE_CAPTURE_LOGGER.error(f"Error creating stop flag: {e}")

    def check_stop_flag(self):
        try:
            if os.path.exists(self.flag_path):
                with open(self.flag_path, 'r') as flag_file:
                    content = flag_file.read().strip()
                    return content.lower() == "true"
            else:
                return False
        except Exception as e:
            IMAGE_CAPTURE_LOGGER.error(f"Error checking stop flag: {e}")
            return False

    def update_stop_flag(self, value):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write(str(value))
        except Exception as e:
            IMAGE_CAPTURE_LOGGER.error(f"Error updating stop flag: {e}")

    def start_service(self):
        try:
            self.running = True
            start_capture = CaptureMain(self.source, self.image_path_to_save, self.image_hash_threshold)
            start_capture.start_stream()
            IMAGE_CAPTURE_LOGGER.info("Image capturing service sucessfully started")

            while self.running:
                time.sleep(1)
                stop_flag = self.check_stop_flag()

                if stop_flag:
                    self.running = False
                    stop_successful = start_capture.stop_stream()
                    if stop_successful:
                        IMAGE_CAPTURE_LOGGER.info("Frame capturing services successfully stopped.")
                    else:
                        IMAGE_CAPTURE_LOGGER.error("Issue encountered while stopping frame capturing services.")

        except Exception as e:
            IMAGE_CAPTURE_LOGGER.error(f"Error starting frame capturing services: {e}")
        finally:
            if 'start_capture' in locals():
                stop_successful = start_capture.stop_stream()
                if stop_successful:
                    IMAGE_CAPTURE_LOGGER.info("Frame capturing services successfully stopped in finally block.")
                else:
                    IMAGE_CAPTURE_LOGGER.error(
                        "Issue encountered while stopping frame capturing services in finally block.")

    def stop_service(self):
        self.update_stop_flag("True")


if __name__ == "__main__":
    FLAG_PATH = "services/alpr/resources/flag_check/capture_status.txt"
    SOURCE = 'rtsp://ishwor:subedi@192.168.1.106:5555/h264_opus.sdp'
    IMAGE_PATH_TO_SAVE = "services/alpr/resources/rtsp/"
    IMAGE_HASH_THRESHOLD = 5

    image_capture_service = StartImageCaptureExample(FLAG_PATH, SOURCE, IMAGE_PATH_TO_SAVE, IMAGE_HASH_THRESHOLD)
    image_capture_service.create_stop_flag()
    image_capture_service.start_service()
    time.sleep(1)
