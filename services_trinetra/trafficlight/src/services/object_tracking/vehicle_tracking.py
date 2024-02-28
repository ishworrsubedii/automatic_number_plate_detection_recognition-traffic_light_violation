import os
import cv2
import random
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort


class ObjectTracker:
    def __init__(self, model_path):
        self.model_path = model_path
        self.target_size = (1280, 723)  # Target size for resizing
        self.confidence_threshold = 0.4
        self.class_colors = {
            'Bicycle': (0, 0, 255),
            'Bus': (0, 255, 255),
            'Car': (0, 127, 255),
            'Motorcycle': (0, 255, 127),
            'Train': (255, 127, 0),
            'Truck': (255, 0, 255),
            # Add more class-color mappings as needed
        }

    def track_images(self, image_dir):
        model = YOLO(self.model_path)
        tracker = DeepSort(max_age=10)

        # Get a list of files in the directory
        image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if
                       f.endswith('.jpg') or f.endswith('.png')]
        image_files.sort(key=os.path.getmtime)  # Sort files by modification time

        for image_path in image_files:
            frame = cv2.imread(image_path)
            if frame is None:
                print(f"Error loading image: {image_path}")
                continue

            frame = cv2.resize(frame, self.target_size)

            detections = model(frame)[0]
            results = []
            for data in detections.boxes.data.tolist():
                confidence = data[4]
                if float(confidence) < self.confidence_threshold:
                    continue
                xmin, ymin, xmax, ymax = map(int, data[:4])
                class_id = int(data[5])
                class_name = model.names[class_id]
                results.append([[xmin, ymin, xmax - xmin, ymax - ymin], confidence, class_name])
            tracks = tracker.update_tracks(results, frame=frame)
            for track in tracks:
                if not track.is_confirmed():
                    continue
                ltrb = track.to_ltrb()
                det_class = track.det_class
                color = self.class_colors.get(det_class,
                                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                xmin, ymin, xmax, ymax = map(int, ltrb[:4])
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
                cv2.putText(frame, f"{det_class}",
                            (xmin + 5, ymin - 8),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.imshow("Frame", frame)
            cv2.waitKey(0)  # Press any key to move to the next image


if __name__ == "__main__":
    model_path = 'services_trinetra/trafficlight/resources/vehicle_detection/yolov8n.pt'
    image_dir = "services_trinetra/trafficlight/resources/rtsp"
    tracker = ObjectTracker(model_path=model_path)
    tracker.track_images(image_dir)
