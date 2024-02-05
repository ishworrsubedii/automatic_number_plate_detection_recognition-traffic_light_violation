"""
Created By: ishwor subedi
Date: 2024-02-05
"""

import os
import time

from services.alpr.src.services.detection.image_capture import CaptureMain


def create_file(filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            f.write('Image capturing started')
    else:
        print(f"File {filename} already exists.")


def check_file_exists(filename):
    return os.path.isfile(filename)


if __name__ == '__main__':
    camera_source = "rtsp://ishwor:subedi@192.168.1.125:5555/h264_opus.sdp"
    image_save_dir = 'services/alpr/resources/rtsp/'
    frame_interval = 10
    capture = CaptureMain(camera_source, image_save_dir, frame_interval)

    flag_file = 'resources/flag_check/capture_status.txt'
    create_file(flag_file)
    capture.start_stream()
    time.sleep(2)
