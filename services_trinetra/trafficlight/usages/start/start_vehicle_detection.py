"""
Created By: ishwor subedi
Date: 2024-02-27
"""

import os
import time

import numpy as np

from services_trinetra.trafficlight.src.services.main_vehicle_det_polygon import VehicleDetectionPolygon


class StartVehicleDetectionExample:
    def __init__(self,
                 flag_path, polygon_points, model_path, detected_images, non_detected_images, red_light_detected,
                 display, red_light_vehicle_detected_path, red_light_vehicle_non_detected_path):

        self.flag_path = flag_path
        self.polygon_points = polygon_points
        self.model_path = model_path
        self.detected_images = detected_images
        self.non_detected_images = non_detected_images

        self.red_light_detected = red_light_detected
        self.display = display

        self.running = False
        self.red_light_vehicle_detected_path = red_light_vehicle_detected_path
        self.red_light_vehicle_non_detected_path = red_light_vehicle_non_detected_path

    def create_stop_flag(self):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write('False')
        except Exception as e:
            print(f"Error creating stop flag: {e}")

    def check_stop_flag(self):
        try:
            if os.path.exists(self.flag_path):
                with open(self.flag_path, 'r') as flag_file:
                    content = flag_file.read().strip()
                    return content.lower() == "true"
            else:
                return False
        except Exception as e:
            print(f"Error checking stop flag: {e}")
            return False

    def update_stop_flag(self, value):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write(str(value))
        except Exception as e:
            print(f"Error updating stop flag: {e}")

    def start_service(self):
        try:
            self.running = True
            vehicle_detector = VehicleDetectionPolygon(polygon_points=self.polygon_points, model_path=self.model_path,
                                                       output_folder=self.detected_images,
                                                       non_detected_images=self.non_detected_images,
                                                       red_light_detected=self.red_light_detected,
                                                       display=self.display,
                                                       red_light_vehicle_non_detected_path=self.red_light_vehicle_non_detected_path,
                                                       red_light_vehicle_detected_path=self.red_light_vehicle_detected_path
                                                       )
            vehicle_detector.start()
            print("Vehicle detection service successfully started")

            while self.running:
                time.sleep(1)
                stop_flag = self.check_stop_flag()

                if stop_flag:
                    self.running = False
                    stop_successful = vehicle_detector.stop()
                    if stop_successful:
                        print("Vehicle detection services successfully stopped.")
                    else:
                        print("Issue encountered while stopping vehicle detection services.")

        except Exception as e:
            print(f"Error starting vehicle detection services: {e}")
        finally:
            if 'vehicle_detector_detector' in locals():
                stop_successful = vehicle_detector.stop()
                if stop_successful:
                    print("Vehicle detection service successfully stopped in finally block.")
                else:
                    print(
                        "Issue encountered while stopping vehicle detection services in finally block.")

    def stop_service(self):
        self.update_stop_flag("True")


if __name__ == '__main__':
    flag_path = "services_trinetra/trafficlight/resources/flag_check/vehicle_det.txt"
    polygon_points = np.array([(615, 340), (909, 346), (1006, 437), (631, 461)])
    model_path = "services_trinetra/trafficlight/resources/vehicle_detection/yolov8n.pt"
    red_light_detected = "services_trinetra/trafficlight/resources/red_light_detected"
    detected_images = "services_trinetra/trafficlight/output/vehicle_detection/detected"
    non_detected_images = "services_trinetra/trafficlight/output/vehicle_detection/non_detected"
    display = False
    red_light_detected_path = "services_trinetra/trafficlight/output/vehicle_detection/detected_images_path"
    red_light_non_detected_path = "services_trinetra/trafficlight/output/vehicle_detection/non_detected_images_path"

    vehicle_detector_server = StartVehicleDetectionExample(
        flag_path=flag_path,
        polygon_points=polygon_points,
        model_path=model_path,
        detected_images=detected_images,
        non_detected_images=non_detected_images,
        red_light_detected=red_light_detected,
        display=display,
        red_light_vehicle_detected_path=red_light_detected_path,
        red_light_vehicle_non_detected_path=red_light_non_detected_path

    )
    vehicle_detector_server.create_stop_flag()
    vehicle_detector_server.start_service()
