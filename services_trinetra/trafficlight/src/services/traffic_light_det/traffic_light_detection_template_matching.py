"""
Created By: ishwor subedi
Date: 2024-02-26
"""
import cv2
import numpy as np


class TrafficLightDetector:
    def __init__(self, template_paths):
        """

        :param template_paths:
        """
        self.templates = [cv2.imread(path, 0) for path in template_paths]

    def template_matching(self, image):
        """

        :param image:
        :return:
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        detected_traffic_lights = []

        for template in self.templates:
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                detected_traffic_lights.append((pt[0], pt[1], pt[0] + w, pt[1] + h))

        return detected_traffic_lights

    def detect_traffic_lights_image(self, image, display: bool):
        result = self.template_matching(image)
        if result:
            cropped_image = None
            for detection in result:
                cv2.rectangle(image, (detection[0], detection[1]), (detection[2], detection[3]), (0, 255, 255), 2)
                cv2.putText(image, 'Traffic Light', (detection[0], detection[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 255), 2)
                cropped_image = image[detection[1]:detection[3], detection[0]:detection[2]]
                if display:
                    cv2.imshow('Traffic Lights Detected', image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
            return cropped_image
        else:
            print("No traffic light detected")
            return None

    def detect_traffic_lights_video(self, display: bool, video_path):
        """

        :param display:
        :param video_path:
        :return:
        """
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            detected_traffic_lights = self.template_matching(frame)

            for bbox in detected_traffic_lights:
                print("Traffic light detected at coordinates:", bbox)

                cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 255), 2)
                cv2.putText(frame, 'Traffic Light', (bbox[0], bbox[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 255), 2)
            if display:
                cv2.imshow('Traffic Lights Detected', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    template_paths = ['services_trinetra/trafficlight/resources/template_images/template1.png',
                      'services_trinetra/trafficlight/resources/template_images/template2.png',
                      'services_trinetra/trafficlight/resources/template_images/template3.png']
    detector = TrafficLightDetector(template_paths)

    # image_detection
    image_path = "/home/ishwor/Pictures/Screenshots/Screenshot from 2024-02-26 17-30-44.png"
    result = detector.detect_traffic_lights_image(image_path, display=True)

    # video_detection
    # video_path = "/home/ishwor/Desktop/dataset/vehicle/video/traffic/VID20240222103234.mp4"
    # result = detector.detect_traffic_lights_video(display=True, video_path=video_path)
    print(result)
