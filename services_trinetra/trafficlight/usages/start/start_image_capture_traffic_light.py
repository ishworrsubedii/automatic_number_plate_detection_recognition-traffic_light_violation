"""
Created By: ishwor subedi
Date: 2024-02-26
"""

import os
import time

from services_trinetra.trafficlight.src.services.capture.image_capture import CaptureMain

from services_trinetra.alpr.usage.start.start_image_capture import StartImageCaptureExample


class StartImageCaptureTrafficLight:
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
            print(e)
            return False

    def update_stop_flag(self, value):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write(str(value))
        except Exception as e:
            print(e)

    def start_service(self):
        try:
            self.running = True
            start_capture = CaptureMain(self.source, self.image_path_to_save, self.image_hash_threshold)
            start_capture.start_stream()
            print("Image capturing service sucessfully started")

            while self.running:
                time.sleep(1)
                stop_flag = self.check_stop_flag()

                if stop_flag:
                    self.running = False
                    stop_successful = start_capture.stop_stream()
                    if stop_successful:
                        print("Frame capturing services_trinetra successfully stopped.")
                    else:
                        print("Issue encountered while stopping frame capturing services_trinetra.")

        except Exception as e:
            print(f"Error starting frame capturing services_trinetra: {e}")
        finally:
            if 'start_capture' in locals():
                stop_successful = start_capture.stop_stream()
                if stop_successful:
                    print("Frame capturing services_trinetra successfully stopped in finally block.")
                else:
                    print(
                        "Issue encountered while stopping frame capturing services_trinetra in finally block.")

    def stop_service(self):
        self.update_stop_flag("True")


if __name__ == "__main__":
    FLAG_PATH = "services_trinetra/trafficlight/resources/flag_check/capture.txt"
    SOURCE = '/home/ishwor/Desktop/dataset/vehicle/video/traffic/VID20240222103234.mp4'
    IMAGE_PATH_TO_SAVE = "services_trinetra/trafficlight/resources/rtsp/"
    IMAGE_HASH_THRESHOLD = 0

    image_capture_service = StartImageCaptureTrafficLight(FLAG_PATH, SOURCE, IMAGE_PATH_TO_SAVE, IMAGE_HASH_THRESHOLD)
    image_capture_service.create_stop_flag()
    image_capture_service.start_service()
    time.sleep(1)
