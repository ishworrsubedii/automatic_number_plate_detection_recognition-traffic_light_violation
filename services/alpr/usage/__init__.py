"""
Created By: ishwor subedi
Date: 2024-02-05
"""

import os
import logging


def configure_logger(logger_name, log_filename, log_dir='logs'):
    log_path = os.path.join(log_dir, log_filename)
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(module)s:%(message)s')

    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


def image_capture_logger(log_dir='services/alpr/logs'):
    return configure_logger('image_cap_logger', 'image_cap_logger.log', log_dir)


def image_load_logger(log_dir='logs'):
    return configure_logger('image_load_logger', 'image_load_logger.log', log_dir)
