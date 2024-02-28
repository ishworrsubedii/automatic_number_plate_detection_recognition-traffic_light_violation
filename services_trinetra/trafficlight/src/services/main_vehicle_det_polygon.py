import os
import threading
import time

import cv2
import numpy as np
from services_trinetra.trafficlight.src.services.detection.vehicle_detection import VehicleDetectionServices


class VehicleDetectionPolygon:
    def __init__(self, polygon_points, model_path, output_folder, display: bool):
        self.polygon_points = polygon_points
        self.image_path = None
        self.display = display
        self.output_folder = output_folder
        self.model_instance = VehicleDetectionServices(model_path)
        self.running = False
        self.vehicle_polygon_detection = None

    def image_path_update(self, image_path):
        self.image_path = image_path

    def polygon_detection(self):
        image = cv2.imread(self.image_path)
        if image is None:
            print("Image not found")
            return

        cv2.polylines(image, [self.polygon_points], True, (0, 255, 255), 2)

        results = self.model_instance.detect_vehicle_image(image_path=self.image_path, confidence_threshold=0.5,
                                                           nms_threshold=0.5)
        desired_classes = [0, 1, 2, 3, 4]
        if results:
            for prediction in results:
                bboxes = prediction.boxes.xyxy
                labels = prediction.boxes.cls

                for id, (bbox, label) in enumerate(zip(bboxes, labels)):
                    if label in desired_classes:
                        x1, y1, x2, y2 = bbox.int().tolist()
                        start_point = (x1, y1)
                        if cv2.pointPolygonTest(self.polygon_points, start_point, False) >= 0:
                            cropped = image[y1:y2, x1:x2]
                            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                            cv2.putText(image, f'Detected', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                        (0, 0, 255), 1)
                            base_name_without_ext = os.path.splitext(os.path.basename(self.image_path))[0]
                            new_image_path = os.path.join(self.output_folder, f'{base_name_without_ext}_{id}.jpg')
                            cv2.imwrite(new_image_path, cropped)
                            print(f"Vehicle detected inside the polygon: {new_image_path}")

                        if self.display:
                            cv2.imshow('Polygon and Detected Vehicles', image)
                            cv2.waitKey(0)
                            cv2.destroyAllWindows()

            else:
                print(f"Vehicle is not inside the polygon{image_path}")


if __name__ == '__main__':
    polygon_points = np.array([(615, 340), (909, 346), (1006, 437), (631, 461)])
    model_path = "services_trinetra/trafficlight/resources/vehicle_detection/yolov8n.pt"
    image_path = "/home/ishwor/Desktop/alpr_speed_traffic/services_trinetra/trafficlight/resources/rtsp/2024-02-28 10:56:46_7.jpg"
    output_folder = "services_trinetra/trafficlight/resources/vehicle_detected"
    display = True
    vehicle_detector = VehicleDetectionPolygon(polygon_points, model_path, output_folder=output_folder,
                                               display=display)
    vehicle_detector.image_path_update(image_path)
    vehicle_detector.polygon_detection()
