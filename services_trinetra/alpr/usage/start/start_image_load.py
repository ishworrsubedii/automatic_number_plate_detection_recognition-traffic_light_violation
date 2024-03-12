import os
import time

from services_trinetra.alpr.src.services.detection.image_load import ImageLoad


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
            print(f"Error creating stop flag: {e}")

    def check_stop_flag(self):
        try:
            if os.path.exists(self.flag_path):
                with open(self.flag_path, 'r') as flag_file:
                    content = flag_file.read().strip()
                    return content.lower() == "true"
            else:
                return False
        except Exception as e:
            print(f"Error checking stop flag: {e}")
            return False

    def update_stop_flag(self, value):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write(str(value))
        except Exception as e:
            print(f"Error updating stop flag: {e}")

    def start_service(self):
        try:
            self.running = True
            start_load = ImageLoad(self.image_dir, self.model_path, self.image_save_dir)
            start_load.start_load_image()
            print("Image loading service successfully started")

            while self.running:
                time.sleep(1)
                stop_flag = self.check_stop_flag()

                if stop_flag:
                    self.running = False
                    stop_successful = start_load.stop_load_image()
                    if stop_successful:
                        print("Image loading services_trinetra successfully stopped.")
                    else:
                        print("Issue encountered while stopping image loading services_trinetra.")

        except Exception as e:
            print(f"Error starting image loading services_trinetra: {e}")
        finally:
            if 'start_load' in locals():
                stop_successful = start_load.stop_load_image()
                if stop_successful:
                    print("Image loading services_trinetra successfully stopped in finally block.")
                else:
                    print(
                        "Issue encountered while stopping image loading services_trinetra in finally block.")

    def stop_service(self):
        self.update_stop_flag("True")


if __name__ == "__main__":
    flag_path = "services_trinetra/alpr/resources/flag_check/start_load_status.txt"
    image_dir = 'services_trinetra/alpr/resources/rtsp/'
    model_path = 'services_trinetra/alpr/resources/yolov8/nnpd.pt'
    image_save_dir = 'services_trinetra/alpr/resources/plate_detected/'

    image_load_service = StartImageLoadExample(flag_path, image_dir, model_path, image_save_dir)
    image_load_service.create_stop_flag()
    image_load_service.start_service()
    time.sleep(1)
