"""
Created By: ishwor subedi
Date: 2024-02-27
"""
import os
import time
from services_trinetra.trafficlight.src.services.main_traffic_light import TrafficLightColorDetection


class StartTrafficLightColorDetectionExample:
    def __init__(self, template_paths, image_directory, red_light_detected, display: bool, flag_path: str = None
                 ):
        self.flag_path = flag_path
        self.display = display
        self.image_dir = image_dir
        self.template_paths = template_paths
        self.red_light_detected = red_light_detected
        self.image_directory = image_directory
        self.running = False

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
            start_traffic_light_detector = TrafficLightColorDetection(
                template_paths=self.template_paths,
                image_directory=self.image_directory,
                red_light_detected=self.red_light_detected,
                display=False
            )
            start_traffic_light_detector.start()
            print("traffic light detection service successfully started")

            while self.running:
                time.sleep(1)
                stop_flag = self.check_stop_flag()

                if stop_flag:
                    self.running = False
                    stop_successful = start_traffic_light_detector.stop()
                    if stop_successful:
                        print("Traffic light detection services successfully stopped.")
                    else:
                        print("Issue encountered while stopping traffic light detection services.")

        except Exception as e:
            print(f"Error starting traffic light detection services: {e}")
        finally:
            if 'start_traffic_light_detector' in locals():
                stop_successful = start_traffic_light_detector.stop()
                if stop_successful:
                    print("Traffic light detection services successfully stopped in finally block.")
                else:
                    print(
                        "Issue encountered while stopping traffic light detection services in finally block.")

    def stop_service(self):
        self.update_stop_flag("True")


if __name__ == '__main__':
    template_paths = ['services_trinetra/trafficlight/resources/template_images/template1.png',
                      'services_trinetra/trafficlight/resources/template_images/template2.png',
                      'services_trinetra/trafficlight/resources/template_images/template3.png']
    image_dir = 'services_trinetra/trafficlight/resources/rtsp'
    red_light_detected = "services_trinetra/trafficlight/resources/red_light_detected"

    display = True
    flag_path = 'services_trinetra/trafficlight/resources/flag_check/traffic_light.txt'

    start_traffic_light_color_detection = StartTrafficLightColorDetectionExample(template_paths=template_paths,
                                                                                 image_directory=image_dir,
                                                                                 display=display,
                                                                                 flag_path=flag_path,
                                                                                 red_light_detected=red_light_detected
                                                                                 )
    start_traffic_light_color_detection.create_stop_flag()
    start_traffic_light_color_detection.start_service()
