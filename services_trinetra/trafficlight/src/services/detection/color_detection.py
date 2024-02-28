import cv2
import numpy as np
from services_trinetra.trafficlight.src.utils.imgutils import resize_image


class ColorFilter:
    def __init__(self):
        self.resized_image = None

    def _load_image(self, image):
        image = resize_image(image, 1280, 723)
        self.resized_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def filter_colors(self, lower_bound, upper_bound):
        hsv_image = cv2.cvtColor(self.resized_image, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        return cv2.bitwise_and(self.resized_image, self.resized_image, mask=mask)

    def calculate_color_percentage(self, filtered_red, filtered_orange, filtered_green):
        red_pixel = np.count_nonzero(filtered_red)
        orange_pixel = np.count_nonzero(filtered_orange)
        green_pixel = np.count_nonzero(filtered_green)

        total_pixels = red_pixel + orange_pixel + green_pixel

        red_percentage = (red_pixel / total_pixels) * 100
        orange_percentage = (orange_pixel / total_pixels) * 100
        green_percentage = (green_pixel / total_pixels) * 100

        return red_percentage, orange_percentage, green_percentage
