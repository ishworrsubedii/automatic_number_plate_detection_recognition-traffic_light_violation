"""
Created By: ishwor subedi
Date: 2024-02-05
"""

import os
import time

from services.alpr.src.services.detection.image_load import ImageLoad


def create_file(filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            f.write('Image capturing started')


def check_file_exists(filename):
    return os.path.isfile(filename)


if __name__ == '__main__':
    image_save_dir = 'services/alpr/resources/rtsp/'
    model_path = 'services/alpr/resources/yolov8/nnpd.pt'
    flag_file = 'resources/flag_check/start_load_status.txt'

    frame_interval = 10
    capture = ImageLoad(image_save_dir, model_path)

    create_file(flag_file)
    capture.start_load_image()
