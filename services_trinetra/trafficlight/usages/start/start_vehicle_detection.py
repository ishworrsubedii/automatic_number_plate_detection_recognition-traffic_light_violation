"""
Created By: ishwor subedi
Date: 2024-02-27
"""
import os

import cv2
import numpy as np

from services_trinetra.trafficlight.src.services.draw.draw_line import DrawService


def vehicle_detection_service(self, filename):
    image_path = os.path.join(self.image_dir, filename)
    image = cv2.imread(image_path)
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, np.array([self.polygon_points], dtype=np.int32), 255)

    masked_image = cv2.bitwise_and(image, mask)

    image_with_polygon = self.draw_service(masked_image)

    results = self.vehicle_detection.detect_image(image_with_polygon, confidence_threshold=0.5, nms_threshold=0.4)
    if results:
        for prediction in results:
            bboxes = prediction.boxes.xyxy

            for i, bbox in enumerate(bboxes):
                multiple_plates = len(bboxes) > 1
                try:
                    bbox = bbox.int().tolist()
                    x1, y1, x2, y2 = bbox
                    cropped = prediction.orig_img[y1:y2, x1:x2]

                    if multiple_plates:
                        filename = f'{self.filename}_plate_{i + 1}.jpg'
                    else:
                        filename = f'{self.filename}.jpg'

                    cv2.imwrite(os.path.join(self.traffic_light_violated_vehicles_images_dir, filename), cropped)

                except:
                    print('No plate detected')


def draw_service(self, image):
    draw_service = DrawService(image)
    draw_service.draw_polygon(self.polygon_points, color=(255, 0, 0), thickness=1)
    return draw_service.image
