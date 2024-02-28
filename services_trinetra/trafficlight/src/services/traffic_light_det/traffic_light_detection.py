from ultralytics.models.yolo import YOLO
from services.alpr.src.entity.service_config import DetectionConfig
import cv2


class TrafficDetectionService:
    def __init__(self, model_path):
        config = DetectionConfig(model_path=model_path)
        self.obj = YOLO(config.model_path)

    def detect_image(self, image_path, confidence_threshold: float, nms_threshold: float):
        """
        Detects vehicle number plate from an image
        :param image_path:  image path to be passed
        :param confidence_threshold:  confidence threshold
        :param nms_threshold:  nms threshold
        :return:  detected results
        """
        img = cv2.imread(image_path)
        results = self.obj.predict(img, conf=confidence_threshold, iou=nms_threshold, show=True)
        return results

    def detect_video(self, video_path: str, display: bool, confidence_threshold: float, nms_threshold: float):
        """
          Detects vehicle number plate from a video
        :param video_path:  video path to be passed
        :param display:  boolean value to display the video
        :param confidence_threshold:  confidence threshold
        :param nms_threshold: nms threshold
        :param class_id: class id of the object to be detected
        :return:  detected results
        """
        cap = cv2.VideoCapture(video_path)
        detections = []
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to read frame")
                break
            frame = cv2.resize(frame, (640, 480))  # Resize the frame
            results = self.obj(frame, conf=confidence_threshold, iou=nms_threshold)
            desired_classes = [9]  # Specify the classes you want to select

            for prediction in results:
                bboxes = prediction.boxes.xyxy
                labels = prediction.boxes.cls
                try:
                    for bbox, label in zip(bboxes,
                                           labels):  # Iterate through all bounding boxes and their corresponding labels
                        x1, y1, x2, y2 = bbox.int().tolist()
                        if label in desired_classes:  # Check if the detected class is one of the desired classes
                            cropped = frame[y1:y2, x1:x2]
                            detections.append((prediction, cropped))
                            if display:
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                                cv2.putText(frame, f'Detected', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                            (0, 0, 255), 2)
                except Exception as e:
                    print(e)

            if display:
                cv2.imshow('frame', frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    cv2.destroyAllWindows()
                    break
        cap.release()
        return detections

    def detect_webcam(self, display: bool, confidence_threshold: float, nms_threshold: float):
        """
        Detects vehicle number plate from a webcam
        :param display: boolean value to display the video
        :param confidence_threshold: confidence threshold
        :param nms_threshold: nms threshold
        :return: detected results
        """
        cap = cv2.VideoCapture(0)
        detections = []
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to read frame")
                break
            frame = cv2.resize(frame, (640, 480))
            results = self.obj(frame, conf=confidence_threshold, iou=nms_threshold)
            for prediction in results:
                bboxes = prediction.boxes.xyxy
                try:
                    bbox = bboxes[0].int().tolist()
                    x1, y1, x2, y2 = bbox
                    cropped = frame[y1:y2, x1:x2]
                    detections.append((prediction, cropped))
                    print(len(detections))
                    if display:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cv2.putText(frame, f'Detected', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                except Exception as e:
                    print(e)
            if display:
                cv2.imshow('frame', frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    cv2.destroyAllWindows()
                    break
        cap.release()
        return detections


if __name__ == '__main__':
    object_instance = TrafficDetectionService(
        model_path='services_trinetra/trafficlight/resources/vehicle_detection/traffic_light.txt.pt')

    # Detect video
    # video_path = '/home/ishwor/Desktop/dataset/vehicle/video/traffic/VID20240222103702.mp4'
    # object_instance.detect_video(video_path, display=True, confidence_threshold=0.5, nms_threshold=0.4)

    # Detect webcam
    # image_path='/home/ishwor/Pictures/Screenshots/Screenshot from 2024-02-26 16-35-17.png'
    # object_instance.detect_image(image_path, display=True, confidence_threshold=0.5, nms_threshold=0.4)

    # Detect image
    image_path = '/home/ishwor/Pictures/Screenshots/Screenshot from 2024-02-26 16-35-17.png'
    object_instance.detect_image(image_path, confidence_threshold=0.5, nms_threshold=0.4)
