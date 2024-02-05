"""
Created By: ishwor subedi
Date: 2024-02-04
"""

import cv2
import os


def image_resize(image, width, height):
    """
    Resize the image to the given width and height
    :param image: image to be resized
    :param width: width of the image
    :param height: height of the image
    :return: resized image
    """
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)


def image_binarization(image, threshold):
    """
    Binarize the image
    :param image: image to be binarized
    :param threshold: threshold value
    :return: binarized image
    """
    return cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]


def get_frame_save_dir(path):


    frame_dir = os.path.join(path)
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)
        print(f"Frame save directory created at {frame_dir}")
    return frame_dir
