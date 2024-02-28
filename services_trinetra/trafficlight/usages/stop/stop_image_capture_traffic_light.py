"""
Created By: ishwor subedi
Date: 2024-02-26
"""

import os


class StopImageCaptureTrafficLight:
    def __init__(self, stop_flag_path):
        self.stop_flag_path = stop_flag_path

    def stop_image_capture_service(self):
        try:
            with open(self.stop_flag_path, 'w') as flag_file:
                flag_file.write("True")
        except Exception as e:
            print(f"Error creating stop flag: {e}")


if __name__ == "__main__":
    STOP_FLAG_PATH = "services_trinetra/trafficlight/resources/flag_check/capture.txt"
    stop_service = StopImageCaptureTrafficLight(STOP_FLAG_PATH)
    stop_service.stop_image_capture_service()
