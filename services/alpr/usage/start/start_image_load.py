import os
import time

from services.alpr.src.services.detection.image_load import ImageLoad
from services.alpr.usage import image_load_logger

IMAGE_LOAD_LOGGER = image_load_logger()


class StartImageLoadExample:
    def __init__(self, flag_path, image_dir, model_path, image_save_dir):
        self.flag_path = flag_path
        self.image_dir = image_dir
        self.model_path = model_path
        self.image_save_dir = image_save_dir

        self.running = False

    def create_stop_flag(self):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write('False')
        except Exception as e:
            IMAGE_LOAD_LOGGER.error(f"Error creating stop flag: {e}")

    def check_stop_flag(self):
        try:
            if os.path.exists(self.flag_path):
                with open(self.flag_path, 'r') as flag_file:
                    content = flag_file.read().strip()
                    return content.lower() == "true"
            else:
                return False
        except Exception as e:
            IMAGE_LOAD_LOGGER.error(f"Error checking stop flag: {e}")
            return False

    def update_stop_flag(self, value):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write(str(value))
        except Exception as e:
            IMAGE_LOAD_LOGGER.error(f"Error updating stop flag: {e}")

    def start_service(self):
        try:
            self.running = True
            start_load = ImageLoad(self.image_dir, self.model_path, self.image_save_dir)
            start_load.start_load_image()
            IMAGE_LOAD_LOGGER.info("Image loading service successfully started")

            while self.running:
                time.sleep(1)
                stop_flag = self.check_stop_flag()

                if stop_flag:
                    self.running = False
                    # Assuming ImageLoad has a stop_load_image method
                    stop_successful = start_load.stop_load_image()
                    if stop_successful:
                        IMAGE_LOAD_LOGGER.info("Image loading services successfully stopped.")
                    else:
                        IMAGE_LOAD_LOGGER.error("Issue encountered while stopping image loading services.")

        except Exception as e:
            IMAGE_LOAD_LOGGER.error(f"Error starting image loading services: {e}")
        finally:
            if 'start_load' in locals():
                stop_successful = start_load.stop_load_image()
                if stop_successful:
                    IMAGE_LOAD_LOGGER.info("Image loading services successfully stopped in finally block.")
                else:
                    IMAGE_LOAD_LOGGER.error(
                        "Issue encountered while stopping image loading services in finally block.")

    def stop_service(self):
        self.update_stop_flag("True")


if __name__ == "__main__":
    flag_path = "services/alpr/resources/flag_check/start_load_status.txt"
    image_dir = 'services/alpr/resources/rtsp/'
    model_path = 'services/alpr/resources/yolov8/nnpd.pt'
    image_save_dir = 'services/alpr/resources/plate_detected/'

    image_load_service = StartImageLoadExample(flag_path, image_dir, model_path, image_save_dir)
    image_load_service.create_stop_flag()
    image_load_service.start_service()
    time.sleep(1)
