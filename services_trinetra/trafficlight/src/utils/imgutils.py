"""
Created By: ishwor subedi
Date: 2024-02-26
"""
import os

import cv2


def resize_image(image, width, height):
    """
    Resize the image to the specified width and height
    :param image: Image to be resized
    :param width: Width of the image
    :param height: Height of the image
    :return: Resized image
    """
    return cv2.resize(image, (width, height))


def image_save(image_save_path, image):
    """

    :param image_save_path:
    :param image:
    :return:
    """
    cv2.imwrite(image_save_path, image)


def check_and_create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory {path} created")


class WriteText:
    def __init__(self, file_path):
        check_and_create_path(file_path)
        self.file_path = file_path

    def write_data(self, data):
        with open(self.file_path, 'w') as file:
            file.write(data)
