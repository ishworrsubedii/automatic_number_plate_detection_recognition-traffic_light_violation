"""
Created By: ishwor subedi
Date: 2024-02-27
"""
import glob
import os
import time
import threading
import warnings
import numpy as np

from services_trinetra.trafficlight.src.services.main_traffic_light import TrafficLightColorDetection
from services_trinetra.trafficlight.src.services.main_vehicle_det_polygon import VehicleDetectionPolygon
import concurrent.futures

warnings.filterwarnings("ignore")


class StartTrafficLightColorDetectionExample:
    def __init__(self, template_paths,
                 image_dir,
                 traffic_light_status,
                 traffic_light_violated_vehicles_images_dir,
                 display,
                 flag_path,
                 polygon_points,
                 model_path):
        self.traffic_light_status = traffic_light_status
        self.flag_path = flag_path
        self.traffic_light_violated_vehicles_images_dir = traffic_light_violated_vehicles_images_dir
        self.display = display
        self.image_dir = image_dir
        self.template_paths = template_paths
        self.start_light_detection_running = False
        self.vehicle_det_running = False
        self.latest_image_path = None
        self.model_path = model_path
        self.poly_points = polygon_points
        self.start_light_detection_service_all = None
        self.start_vehicle_detection_service_all = None
        self.vehicle_detection_polygon = VehicleDetectionPolygon(model_path=self.model_path,
                                                                 polygon_points=self.poly_points,
                                                                 output_folder=self.traffic_light_violated_vehicles_images_dir,
                                                                 display=False)
        self.traffic_light_detector = TrafficLightColorDetection(template_paths=self.template_paths,
                                                                 traffic_light_result_file_path=self.traffic_light_status
                                                                 , display=False)

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
            print("Error checking stop flag: {e}")
            return False

    def update_stop_flag(self, value):
        try:
            with open(self.flag_path, 'w') as flag_file:
                flag_file.write(str(value))
        except Exception as e:
            print(f"Error updating stop flag: {e}")

    def read_file_concurrently(self, file_path):
        def read_file(file_path):
            with open(file_path, 'r') as file:
                content = file.read().strip()
            return content

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(read_file, file_path)
            return future.result()

    def start_light_detection_services(self):
        self.start_light_detection_running = True
        self.start_light_detection_service_all = threading.Thread(target=self.traffic_light_main)
        self.start_light_detection_service_all.start()

    def start_vehicle_detection_services(self):
        self.vehicle_det_running = True
        self.start_vehicle_detection_service_all = threading.Thread(target=self.vehicle_detection_main)
        self.start_vehicle_detection_service_all.start()

    def stop_light_detection_services(self):
        if self.start_light_detection_running:
            self.start_light_detection_service_all.join()
        self.start_light_detection_running = False

    def stop_vehicle_detection_services(self):
        if self.vehicle_det_running:
            self.start_vehicle_detection_service_all.join()
        self.vehicle_det_running = False

    def traffic_light_main(self):
        self.traffic_light_detector.image_path_update(self.latest_image_path)
        self.traffic_light_detector.process_image()

    def vehicle_detection_main(self):
        self.vehicle_detection_polygon.image_path_update(self.latest_image_path)
        self.vehicle_detection_polygon.polygon_detection()

    def start_service(self):
        try:
            while True:
                image_files = glob.glob(os.path.join(self.image_dir, '*'))
                sorted_files = sorted(image_files, key=os.path.getctime)
                if sorted_files and sorted_files[0] != self.latest_image_path:
                    self.latest_image_path = sorted_files[0]
                    print(f"Processing image: {self.latest_image_path}")

                    self.start_light_detection_services()
                    traffic_light_status = self.read_file_concurrently(self.traffic_light_status)

                    if traffic_light_status.lower() == 'red light':
                        print("Traffic light is red. Starting vehicle detection services.")
                        self.start_vehicle_detection_services()

                    if self.start_light_detection_running and (
                            self.vehicle_det_running or traffic_light_status.lower() != 'red light'):
                        if self.latest_image_path and os.path.exists(self.latest_image_path):
                            print(f"Removing processed image: {self.latest_image_path}")
                            os.remove(self.latest_image_path)

                    stop_flag = self.check_stop_flag()

                    if stop_flag:
                        self.start_light_detection_running = False
                        self.vehicle_det_running = False
                        stop_successful_traffic_light_detector = self.stop_light_detection_services() and self.stop_vehicle_detection_services()
                        if stop_successful_traffic_light_detector:
                            print("Image loading services stopped successfully.")
                        else:
                            print("An issue was encountered while stopping image loading services.")

        except Exception as e:
            print(f"An error occurred while starting image loading services: {e}")

        finally:
            if 'start_all_services' in locals():
                stop_successful = self.stop_light_detection_services() and self.stop_vehicle_detection_services()
                if stop_successful:
                    print("Image loading services stopped successfully in the finally block.")
                else:
                    print("An issue was encountered while stopping image loading services in the finally block.")

    def stop_services(self):
        self.update_stop_flag("True")


if __name__ == '__main__':
    template_paths = ['services_trinetra/trafficlight/resources/template_images/template1.png',
                      'services_trinetra/trafficlight/resources/template_images/template2.png',
                      'services_trinetra/trafficlight/resources/template_images/template3.png']
    image_dir = 'services_trinetra/trafficlight/resources/rtsp'
    traffic_light_status = 'services_trinetra/trafficlight/resources/flag_check/light_status'
    traffic_light_violated_vehicles_images_dir = 'services_trinetra/trafficlight/resources/vehicle_detected'
    display = True
    flag_path = 'services_trinetra/trafficlight/resources/flag_check/traffic_light_color_vehicle_detection'
    polygon_points = np.array([(615, 340), (909, 346), (1006, 437), (631, 461)])
    model_path = 'services_trinetra/trafficlight/resources/vehicle_detection/vd.pt'

    start_traffic_light_color_detection = StartTrafficLightColorDetectionExample(display=display,
                                                                                 traffic_light_violated_vehicles_images_dir=traffic_light_violated_vehicles_images_dir,
                                                                                 traffic_light_status=traffic_light_status,
                                                                                 flag_path=flag_path,
                                                                                 image_dir=image_dir,
                                                                                 template_paths=template_paths,
                                                                                 polygon_points=polygon_points,
                                                                                 model_path=model_path
                                                                                 )
    start_traffic_light_color_detection.create_stop_flag()
    start_traffic_light_color_detection.start_service()
