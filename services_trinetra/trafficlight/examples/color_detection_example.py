"""
Created By: ishwor subedi
Date: 2024-02-26
"""
import configparser

import cv2
import numpy as np

from services_trinetra.trafficlight.src.services.detection.color_detection import ColorFilter

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('services_trinetra/trafficlight/config/config.ini')

    image_path = config['Paths']['image_path']
    red_lower = np.array(list(map(int, config['Colors']['red_lower'].split(','))))
    red_upper = np.array(list(map(int, config['Colors']['red_upper'].split(','))))
    orange_lower = np.array(list(map(int, config['Colors']['orange_lower'].split(','))))
    orange_upper = np.array(list(map(int, config['Colors']['orange_upper'].split(','))))
    green_lower = np.array(list(map(int, config['Colors']['green_lower'].split(','))))
    green_upper = np.array(list(map(int, config['Colors']['green_upper'].split(','))))
    image = cv2.imread(image_path)
    color_filter = ColorFilter()
    color_filter._load_image(image)

    filtered_red = color_filter.filter_colors(red_lower, red_upper)
    filtered_orange = color_filter.filter_colors(orange_lower, orange_upper)
    filtered_green = color_filter.filter_colors(green_lower, green_upper)

    red_percentage, orange_percentage, green_percentage = color_filter.calculate_color_percentage(filtered_red,
                                                                                                  filtered_orange,
                                                                                                  filtered_green)

    print(f"Red percentage: {red_percentage:.2f}%")
    print(f"Orange percentage: {orange_percentage:.2f}%")
    print(f"Green percentage: {green_percentage:.2f}%")
