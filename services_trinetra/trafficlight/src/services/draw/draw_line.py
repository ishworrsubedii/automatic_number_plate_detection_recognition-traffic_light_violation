"""
Created By: ishwor subedi
Date: 2024-02-26
"""
import cv2
from PIL.Image import Image
import numpy as np


class DrawService:
    def __init__(self, image):
        self.image = image

    def draw_line(self, point_a, point_b, color=(255, 0, 0), thickness=2):
        cv2.line(self.image, point_a, point_b, color, thickness)

    def draw_polygon(self, points, color=(255, 0, 0), thickness=2):
        points_array = np.array(points, np.int32)
        points_array = points_array.reshape((-1, 1, 2))
        cv2.polylines(self.image, [points_array], True, color, thickness)


if __name__ == '__main__':
    path = '/home/ishwor/Pictures/Screenshots/Screenshot from 2024-02-26 15-54-01.png'
    image = cv2.imread(path)
    draw_service = DrawService()
    # resize_image(draw_service.image, 1280, 723)

    draw_service.draw_polygon([(645, 306), (848, 315), (890, 345), (647, 332)])
    cv2.imwrite(path, draw_service.image)
    cv2.imshow('Image', draw_service.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
