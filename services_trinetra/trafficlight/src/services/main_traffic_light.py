import os.path
from concurrent.futures import ThreadPoolExecutor
import cv2
from services_trinetra.trafficlight.src.services.traffic_light_det.traffic_light_detection_template_matching import \
    TrafficLightDetector
from services_trinetra.trafficlight.src.services.detection.color_detection import ColorFilter
from services_trinetra.trafficlight.src.utils.imgutils import WriteText, resize_image


class TrafficLightColorDetection:

    def __init__(self, template_paths
                 , traffic_light_result_file_path, display: bool):
        self.write_status = WriteText(file_path=traffic_light_result_file_path)
        self.traffic_light_detection = TrafficLightDetector(template_paths)
        self.red_upper = 10, 255, 255
        self.red_lower = 0, 100, 100
        self.orange_upper = 25, 255, 255
        self.orange_lower = 11, 100, 100
        self.green_upper = 85, 255, 255
        self.green_lower = 35, 100, 100
        self.display = display
        self.start_traffic_light_det = None
        self.image = None
        self.latest_image_path = None

        try:
            self.color_detection_traffic_light_service = ColorFilter()
        except Exception as e:
            print(f"Error creating ColorFilter object: {e}")
            self.color_detection_traffic_light_service = None

        self.running = False

    def read(self):
        try:
            image = cv2.imread(self.latest_image_path)
            if image is not None:
                self.image = image
        except Exception as e:
            print(f"Error reading image: {e}")

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
                self.write_status.write_data(f"Red Light")
                cv2.putText(self.image, 'Red Light', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            elif orange_percentage > 60:
                self.write_status.write_data(f"Orange Light")
                cv2.putText(self.image, 'Orange Light', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)
            elif green_percentage > 60:
                self.write_status.write_data(f"Green Light")
                cv2.putText(self.image, 'Green Light', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                self.write_status.write_data(f"No Light")
                cv2.putText(self.image, 'No Light', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        except Exception as e:
            print(f"Error in color detection service: {e}")

    def traffic_light_detection_service(self, image):
        try:
            cropped_image = self.traffic_light_detection.detect_traffic_lights_image(image, display=False)
            if cropped_image is None:
                return None
            else:
                return cropped_image
        except Exception as e:
            print(f"Error in traffic light detection service: {e}")
            return None

    def image_path_update(self, image_path):
        self.latest_image_path = image_path

    def process_image(self):
        if self.latest_image_path is not None:
            image = cv2.imread(self.latest_image_path)

            with ThreadPoolExecutor(max_workers=10) as executor:
                try:
                    future = executor.submit(self.traffic_light_detection_service, image)
                    cropped_image = future.result()
                    if cropped_image is not None:
                        future = executor.submit(self.color_detection_service, cropped_image)
                        future.result()

                        print(f"Processing image {self.latest_image_path}")
                        print("-----------------------------------------------------------------------\n")
                        if self.display:
                            cv2.namedWindow('Traffic Light Detection', cv2.WINDOW_NORMAL)
                            cv2.imshow('Traffic Light Detection', image)
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                return

                    else:
                        print("**********************************************************************\n")
                        print(f"No any traffic light detected")
                except Exception as e:
                    print(f"Error processing image {self.latest_image_path}: {e}")

        else:
            print("Image Path None")


if __name__ == '__main__':
    template_paths = ['services_trinetra/trafficlight/resources/template_images/template1.png',
                      'services_trinetra/trafficlight/resources/template_images/template2.png',
                      'services_trinetra/trafficlight/resources/template_images/template3.png']
    image_path = "services_trinetra/trafficlight/resources/rtsp/2024-02-27 22:29:24_6.jpg"
    if os.path.exists(image_path):
        print("Image exists")
    else:
        print("Image does not exist")

    traffic_light_violated_vehicles_images_dir = "services_trinetra/trafficlight/resources/vehicle_detected"

    try:
        traffic_light_detector = TrafficLightColorDetection(
            template_paths,
            traffic_light_result_file_path='services_trinetra/trafficlight/resources/flag_check/light_status',
            display=True
        )
        traffic_light_detector.image_path_update(image_path)
        traffic_light_detector.process_image()
    except Exception as e:
        print(f"Error in main: {e}")
