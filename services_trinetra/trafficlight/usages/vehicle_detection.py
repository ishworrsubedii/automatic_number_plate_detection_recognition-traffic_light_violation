"""
Created By: ishwor subedi
Date: 2024-02-07
"""
from services_trinetra.alpr.src.entity.service_config import DetectionConfig
from services_trinetra.alpr.src.services.detection.vehicle_number_plate_detection import DetectionService

if __name__ == '__main__':
    config = DetectionConfig(model_path='services_trinetra/trafficlight/resources/vehicle_detection/vd.pt')
    service = DetectionService(config)

    # Detect webcam
    # service.detect_webcam(display=True, confidence_threshold=0.5, nms_threshold=0.4)

    # Detect image
    # service.detect_image('/home/ishwor/Pictures/Screenshots/Screenshot from 2024-02-03 20-41-34.png',
    #                      confidence_threshold=0.5, nms_threshold=0.4)

    # Detect videos
    service.detect_video(
        '/home/ishwor/Desktop/dataset/videos/videoplayback.mp4',
        display=True, confidence_threshold=0.5, nms_threshold=0.4)
