"""
Created By: ishwor subedi
Date: 2024-02-26
"""
import cv2

from services_trinetra.alpr.src.services.detection.vehicle_number_plate_detection import DetectionService
from services_trinetra.alpr.src.entity.service_config import DetectionConfig


class VehicleDetectionServices:
    def __init__(self, model_path: str):
        config = DetectionConfig(model_path=model_path)
        self.obj = DetectionService(config)

    def detect_vehicle_image(self, image_path, confidence_threshold: float, nms_threshold: float):
        results = self.obj.detect_image(image_path, confidence_threshold, nms_threshold, display=False)

        return results

    def detect_vehicle_video(self, video_path: str, display: bool, confidence_threshold: float, nms_threshold: float):
        results = self.obj.detect_video(video_path, display, confidence_threshold, nms_threshold)
        return results


if __name__ == '__main__':
    model_path = 'services_trinetra/trafficlight/resources/vehicle_detection/vd.pt'
    image_path = '/home/ishwor/Pictures/Screenshots/Screenshot from 2024-02-27 10-29-34.png'
    model_instance = VehicleDetectionServices(model_path)
    res = model_instance.detect_vehicle_image(image_path=image_path, confidence_threshold=0.5,
                                              nms_threshold=0.5)
