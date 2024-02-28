"""
Created By: ishwor subedi
Date: 2024-02-26
"""
import cv2
from services_trinetra.trafficlight.src.utils.imgutils import resize_image


class TrafficDetectionService:
    def __init__(self, detection_point: str):
        """

        :param detection_point:
        """
        self.detection_point = detection_point
        pass

    def detect_image(self, img_path: str, display: bool):
        """

        :param img_path:
        :param display:
        :return:
        """

        image = cv2.imread(img_path)
        image = resize_image(image, 1280, 723)

        if display:
            cv2.rectangle(image, (self.detection[0], self.detection[1]), (self.detection[2], self.detection[3]),
                          (0, 255, 255), 2)
            cv2.putText(image, 'Traffic Light', (self.detection[0], self.detection[1] - 5), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 255), 2)
            if display:
                cv2.imshow('Traffic Lights Detected', image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    def detect_video(self, video_path, display: bool):
        """

        :param video_path:
        :param display:
        :return:
        """
        detection = self.parse_detection_point()
        if not detection:
            return

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("Error: Could not open video file.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.rectangle(frame, (detection[0], detection[1]), (detection[2], detection[3]), (0, 255, 255), 2)
            cv2.putText(frame, 'Traffic Light', (detection[0], detection[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 255), 2)

            if display:
                cv2.imshow('Traffic Lights Detected', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    # detect image
    #     object_instance = TrafficDetectionService(detection_point=(50, 50, 100, 100))
    #     object_instance.detect_image(img_path='path/to/image', display=True)
    # detect video
    object_instance = TrafficDetectionService(detection_point=(50, 50, 100, 100))
    object_instance.detect_video(video_path='path/to/video', display=True)
