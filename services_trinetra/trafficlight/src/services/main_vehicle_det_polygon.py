import threading
import os
import sys
import time

import cv2
import numpy as np
from services_trinetra.trafficlight.src.services.detection.vehicle_detection import VehicleDetectionServices
import warnings

warnings.filterwarnings("ignore")


class VehicleDetectionPolygon:
    def __init__(self, polygon_points, model_path, output_folder, non_detected_images, red_light_detected,
                 display: bool, red_light_vehicle_detected_path, red_light_vehicle_non_detected_path):
        self.polygon_points = polygon_points
        self.display = display
        self.detected_image_dir = output_folder
        self.non_detected_images = non_detected_images

        self.model_instance = VehicleDetectionServices(model_path)
        self.thread_running = False
        self.vehicle_polygon_detection = None
        self.red_light_detected = red_light_detected

        self.latest_image_path = None
        self.process = None
        self.red_light_vehicle_detected_path = red_light_vehicle_detected_path
        self.red_light_vehicle_non_detected_path = red_light_vehicle_non_detected_path

    def image_save(self, image, image_path):
        cv2.imwrite(image_path, image)

    def polygon_detection(self):
        while self.thread_running:

            image_lists = os.listdir(self.red_light_detected)
            for image_path in image_lists:
                self.latest_image_path = os.path.join(self.red_light_detected, image_path)

                image = cv2.imread(self.latest_image_path)

                try:
                    results = self.model_instance.detect_vehicle_image(image_path=self.latest_image_path,
                                                                       confidence_threshold=0.5,
                                                                       nms_threshold=0.5)
                except FileNotFoundError:
                    print(f"File not found: {self.latest_image_path}")
                    continue

                desired_classes = [0, 1, 2, 3, 4]
                detected = False
                if results and self.thread_running:
                    for prediction in results:
                        bboxes = prediction.boxes.xyxy
                        labels = prediction.boxes.cls

                        for id, (bbox, label) in enumerate(zip(bboxes, labels)):
                            if label in desired_classes:
                                x1, y1, x2, y2 = bbox.int().tolist()
                                start_point = (x1, y1)
                                if cv2.pointPolygonTest(self.polygon_points, start_point,
                                                        False) >= 0 and self.thread_running:
                                    cropped = image[y1:y2, x1:x2]

                                    base_name_without_ext = os.path.splitext(os.path.basename(self.latest_image_path))[
                                        0]
                                    new_image_path = os.path.join(self.detected_image_dir,
                                                                  f'{base_name_without_ext}_{id}.jpg')
                                    self.image_save(cropped, new_image_path)
                                    with open(self.red_light_vehicle_detected_path, 'a') as file:
                                        file.write(f"Detected_image_path:{new_image_path}\n")
                                    print(f"Vehicle detected inside the polygon: {new_image_path}")
                                    detected = True

                else:
                    pass
                    print("No vehicle detected")

                if not detected and self.thread_running:
                    base_name_without_ext = os.path.splitext(os.path.basename(self.latest_image_path))[0]
                    new_image_path = os.path.join(self.non_detected_images, f'{base_name_without_ext}.jpg')
                    with open(self.red_light_vehicle_non_detected_path, 'a') as file:
                        file.write(f"Non_detected_image_path:{new_image_path}\n")
                    if image is not None:
                        cv2.imwrite(new_image_path, image)
                    else:
                        pass

                os.remove(self.latest_image_path)
        time.sleep(0.01)

    def start(self):
        self.thread_running = True
        self.process = threading.Thread(target=self.polygon_detection)
        self.process.start()

    def stop(self):
        print("Stopping the process...")
        if self.thread_running:
            self.thread_running = False
            self.process.join()
        else:
            print("Thread is not running")

        print("Exiting the program...")
        sys.exit()


if __name__ == '__main__':
    polygon_points = np.array([(615, 340), (909, 346), (1006, 437), (631, 461)])
    model_path = "services_trinetra/trafficlight/resources/vehicle_detection/yolov8n.pt"
    red_light_detected = "services_trinetra/trafficlight/resources/red_light_detected"
    detected_images = "services_trinetra/trafficlight/output/vehicle_detection/detected"
    non_detected_images = "services_trinetra/trafficlight/output/vehicle_detection/non_detected"
    red_light_detected_path = "services_trinetra/trafficlight/output/vehicle_detection/detected_images_path.txt"
    red_light_non_detected_path = "services_trinetra/trafficlight/output/vehicle_detection/non_detected_images_path.txt"

    display = False
    vehicle_detector = VehicleDetectionPolygon(polygon_points, model_path, output_folder=detected_images,
                                               non_detected_images=non_detected_images,
                                               red_light_detected=red_light_detected,
                                               display=display,
                                               red_light_vehicle_detected_path=red_light_detected_path,
                                               red_light_vehicle_non_detected_path=red_light_non_detected_path)
    vehicle_detector.start()
    time.sleep(2)
    vehicle_detector.stop()
