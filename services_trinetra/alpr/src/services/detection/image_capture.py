import imagehash
import threading
import cv2
import os
from PIL import Image
from datetime import datetime
import time

from services.alpr.src.utils.imageutils import get_frame_save_dir


class CaptureMain:
    def __init__(self, camera_source, image_save_dir, frame_interval):
        self.camera_source = camera_source
        if os.path.exists(image_save_dir):
            self.image_path_to_save = image_save_dir

        else:
            self.image_path_to_save = get_frame_save_dir(image_save_dir)

        self.frame_interval = frame_interval
        self.cap = cv2.VideoCapture(self.camera_source)
        self.thread_running = False

    def start_stream(self):
        self.frame_save_thread = threading.Thread(target=self.frame_extraction_from_camera)
        self.frame_save_thread.start()
        self.thread_running = True

    def stop_stream(self):
        if self.thread_running:
            self.thread_running = False
            self.cap.release()

            self.frame_save_thread.join()

    def image_hashing(self, previous_frame, current_frame):

        if previous_frame is None:
            return None
        else:
            hash1 = imagehash.average_hash(Image.fromarray(previous_frame))
            hash2 = imagehash.average_hash(Image.fromarray(current_frame))
        return hash1 - hash2

    def frame_extraction_from_camera(self):
        try:
            previous_frame = None
            while self.cap.isOpened():
                success, frame = self.cap.read()
                if success:
                    hash_diff = self.image_hashing(previous_frame, frame)
                    if hash_diff is None or hash_diff > self.frame_interval:
                        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        name = os.path.join(self.image_path_to_save, f"{current_time}.jpg")
                        success = cv2.imwrite(name, frame)
                        if success:
                            print(f"Frame saved at {name}")
                        else:
                            print(f"Failed to save frame at {name}")

                    previous_frame = frame
        except Exception as e:
            try:
                self.stop_stream()
            except Exception as e:
                print(f"An error occurred while stopping the stream: {e}")

#
# if __name__ == '__main__':
#     try:
#         camera_source = "rtsp://ishwor:subedi@192.168.1.125:5555/h264_opus.sdp"
#         image_save_dir = 'services/alpr/resources/rtsp/'
#         frame_interval = 10
#         capture = CaptureMain(camera_source, image_save_dir, frame_interval)
#         try:
#             capture.start_stream()
#         except Exception as e:
#             print(f"An error occurred while starting the stream: {e}")
#             capture.stop_stream()
#             raise e
#
#         while capture.thread_running:
#             time.sleep(1)
#
#     except KeyboardInterrupt:
#         print("Interrupted, stopping the stream.")
#         capture.stop_stream()
#     except cv2.error as e:
#         print(f"OpenCV error occurred: {e}")
#         capture.stop_stream()
#     except OSError as e:
#         print(f"OS error occurred: {e}")
#         capture.stop_stream()
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         capture.stop_stream()
