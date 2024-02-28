"""
Created By: ishwor subedi
Date: 2024-02-05
"""


class StopImageCaptureExample:
    def __init__(self, stop_flag_path):
        self.stop_flag_path = stop_flag_path

    def stop_image_capture_service(self):
        try:
            with open(self.stop_flag_path, 'w') as flag_file:
                flag_file.write("True")
        except Exception as e:
            print(f"Error updating stop flag :{e}")


if __name__ == "__main__":
    STOP_FLAG_PATH = "services_trinetra/alpr/resources/flag_check/capture_status.txt"
    stop_service = StopImageCaptureExample(STOP_FLAG_PATH)
    stop_service.stop_image_capture_service()
