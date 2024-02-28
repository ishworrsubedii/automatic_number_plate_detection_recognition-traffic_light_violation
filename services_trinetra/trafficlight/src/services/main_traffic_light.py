import multiprocessing
import os
import time
import sys

import cv2

from services_trinetra.trafficlight.src.services.traffic_light_det.traffic_light_detection_template_matching import \
    TrafficLightDetector
from services_trinetra.trafficlight.src.services.detection.color_detection import ColorFilter


class TrafficLightColorDetection:
    def __init__(self, template_paths, image_directory, red_light_detected,
                 display: bool):
        self.red_light_detected_dir = red_light_detected
        self.image_directory = image_directory
        self.template_paths = template_paths

        self.red_upper = 10, 255, 255
        self.red_lower = 0, 100, 100
        self.orange_upper = 25, 255, 255
        self.orange_lower = 11, 100, 100
        self.green_upper = 85, 255, 255
        self.green_lower = 35, 100, 100
        self.display = display
        self.latest_image_path = None
        self.color_detection_traffic_light_service = ColorFilter()
        self.thread_running = False
        self.image = None
        self.process = None

    def color_detection_service(self, cropped_image):
        try:
            self.color_detection_traffic_light_service._load_image(cropped_image)
            filtered_red = self.color_detection_traffic_light_service.filter_colors(self.red_lower, self.red_upper)
            filtered_orange = self.color_detection_traffic_light_service.filter_colors(self.orange_lower,
                                                                                       self.orange_upper)
            filtered_green = self.color_detection_traffic_light_service.filter_colors(self.green_lower,
                                                                                      self.green_upper)
            red_percentage, orange_percentage, green_percentage = self.color_detection_traffic_light_service.calculate_color_percentage(
                filtered_red,
                filtered_orange,
                filtered_green)
            print(f"Red: {int(red_percentage)}%, Orange: {int(orange_percentage)}%, Green: {int(green_percentage)}%")

            if red_percentage > 5:
                cv2.putText(self.image, 'Red Light', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                new_image_path_without_extension = os.path.splitext(os.path.basename(self.latest_image_path))[0]
                new_image_path = os.path.join(self.red_light_detected_dir, f"{new_image_path_without_extension}.jpg")
                cv2.imwrite(new_image_path, self.image)

            elif orange_percentage > 60:
                cv2.putText(self.image, 'Orange Light', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)
            elif green_percentage > 60:
                cv2.putText(self.image, 'Green Light', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(self.image, 'No Light', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        except Exception as e:
            print(f"Error in color detection service: {e}")

    def traffic_light_detection_service(self, image):
        try:
            traffic_light_detection = TrafficLightDetector(self.template_paths)

            cropped_image = traffic_light_detection.detect_traffic_lights_image(image, display=False)
            if cropped_image is not None:
                self.color_detection_service(cropped_image)
            else:
                print("No any traffic light detected")
        except Exception as e:
            print(f"Error in traffic light detection service: {e}")

    def process_image(self):
        while self.thread_running:
            image_list = sorted(os.listdir(self.image_directory))
            for image_path in image_list:

                self.latest_image_path = os.path.join(self.image_directory, image_path)

                self.image = cv2.imread(self.latest_image_path)
                if self.image is not None and self.thread_running:
                    self.traffic_light_detection_service(self.image)
                    print(f"Processing image {self.latest_image_path}")
                    print("-----------------------------------------------------------------------\n")
                    os.remove(self.latest_image_path)
                    if self.display and self.thread_running:  # Add check here
                        cv2.namedWindow('Traffic Light Detection', cv2.WINDOW_NORMAL)
                        cv2.imshow('Traffic Light Detection', self.image)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            return
                else:
                    print("Error reading image")

    def start(self):
        self.thread_running = True
        self.process = multiprocessing.Process(target=self.process_image)
        self.process.start()

    def stop(self):
        print("Stopping the process...")
        if self.thread_running:
            if self.process.is_alive():
                self.process.terminate()
                self.process.join()

        self.thread_running = False
        print("Exiting the program...")
        sys.exit()


if __name__ == '__main__':
    template_paths = ['services_trinetra/trafficlight/resources/template_images/template1.png',
                      'services_trinetra/trafficlight/resources/template_images/template2.png',
                      'services_trinetra/trafficlight/resources/template_images/template3.png']
    image_directory = "services_trinetra/trafficlight/resources/rtsp"
    red_light_detected = "services_trinetra/trafficlight/resources/red_light_detected"

    if not os.path.exists(image_directory):
        print("Image directory does not exist")
        exit(10)

    traffic_light_detector = TrafficLightColorDetection(
        template_paths=template_paths,
        image_directory=image_directory,
        red_light_detected=red_light_detected,
        display=False
    )
    traffic_light_detector.start()
    time.sleep(1)
    traffic_light_detector.stop()
