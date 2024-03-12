from ultralytics.models.yolo import YOLO
from services_trinetra.alpr.src.entity.service_config import DetectionConfig
import cv2


class DetectionService:
    def __init__(self, config: DetectionConfig):
        self.model_instance = YOLO(config.model_path)

    def detect_image(self, image, confidence_threshold: float, nms_threshold: float, display: bool):
        """
        Detects vehicle number plate from an image
        :param image_path:  image path to be passed
        :param confidence_threshold:  confidence threshold
        :param nms_threshold:  nms threshold
        :return:  detected results
        """

        results = self.model_instance.predict(image, conf=confidence_threshold, iou=nms_threshold, show=display)

        # for prediction in results:
        #     bboxes = prediction.boxes.xyxy
        #     try:
        #         bbox = bboxes[0].int().tolist()
        #         x1, y1, x2, y2 = bbox
        #         cropped = img[y1:y2, x1:x2]
        #
        #         return prediction, cropped
        #
        #     except Exception as e:
        #         print(e)
        return results

    def detect_video(self, video_path: str, display: bool, confidence_threshold: float, nms_threshold: float):
        """
          Detects vehicle number plate from a video
        :param video_path:  video path to be passed
        :param display:  boolean value to display the video
        :param confidence_threshold:  confidence threshold
        :param nms_threshold: nms threshold
        :return:  detected results
        """
        cap = cv2.VideoCapture(video_path)
        detections = []
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to read frame")
                break
            frame = cv2.resize(frame, (640, 480))
            results = self.model_instance(frame, conf=confidence_threshold, iou=nms_threshold)
            for prediction in results:
                bboxes = prediction.boxes.xyxy
                try:
                    bbox = bboxes[0].int().tolist()
                    x1, y1, x2, y2 = bbox
                    cropped = frame[y1:y2, x1:x2]
                    detections.append((prediction, cropped))
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

    def detect_webcam(self, display: bool, confidence_threshold: float, nms_threshold: float):
        """
        Detects vehicle number plate from a webcam
        :param display: boolean value to display the video
        :param confidence_threshold: confidence threshold
        :param nms_threshold: non-maximum suppression threshold
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
            results = self.model_instance(frame, conf=confidence_threshold, iou=nms_threshold)
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
    config = DetectionConfig(model_path='services_trinetra/alpr/resources/yolov8/nnpd.pt')
    service = DetectionService(config)

    # Detect webcam
    service.detect_webcam(display=True, confidence_threshold=0.5, nms_threshold=0.4)

    # Detect image
    # service.detect_image('/home/ishwor/Pictures/Screenshots/Screenshot from 2024-02-03 20-41-34.png',
    #                      confidence_threshold=0.5, nms_threshold=0.4)

    # Detect video
    # service.detect_video(
    #     '/home/ishwor/Desktop/TreeLeaf/Vehicle Number Plate/Dataset/cam_back_2022_09_02/videos/ipcam__1.mp4',
    #     display=True, confidence_threshold=0.5, nms_threshold=0.4)
