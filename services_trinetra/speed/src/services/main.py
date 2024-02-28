"""
Created By: ishwor subedi
Date: 2024-02-19
"""
import cv2
import numpy as np
import supervision as sv
from ultralytics import YOLO

from collections import defaultdict, deque
from services_trinetra.speed.src.services.speed.speed_estimation import speed_estimation
from services_trinetra.speed.src.services.tracking.object_tracking import object_tracking
from services_trinetra.speed.src.services.detection.object_detection import ObjectDetectionService, PerspectiveTransformer

TARGET_WIDTH = 10
TARGET_HEIGHT = 250  # in meters

TARGET = np.array(
    [[0, 0],
     [TARGET_WIDTH - 1, 0],
     [TARGET_WIDTH - 1, TARGET_HEIGHT - 1],
     [0, TARGET_HEIGHT - 1]
     ]
)


class SpeedEstimationService(ObjectDetectionService):
    def __init__(self, model_path, source):

        super().__init__(model_path, source)

    def video_process_supervision(self, source, display):
        """
        Video process supervision
        :param source:  source of video
        :param display: display video or not
        :return:
        """
        SOURCE = np.array([[
            [
                61.66129032258068,
                720.2741935483871
            ],
            [
                372.1451612903226,
                205.75806451612902
            ],
            [
                631.8225806451613,
                198.5
            ],
            [
                988.2741935483871,
                720.2741935483871
            ]
        ]]).astype(int)

        byte_track = object_tracking(self.video_info)
        thickness = sv.calculate_dynamic_line_thickness(resolution_wh=self.video_info.resolution_wh)
        text_scale = sv.calculate_dynamic_text_scale(resolution_wh=self.video_info.resolution_wh)
        bounding_box_annotator = sv.BoundingBoxAnnotator(thickness=2)
        label_annotator = sv.LabelAnnotator(text_scale=text_scale, text_thickness=thickness)

        trace_annotator = sv.TraceAnnotator(
            thickness=thickness,
            trace_length=self.video_info.fps * 2,
            position=sv.Position.BOTTOM_CENTER,
        )
        frame_generator = sv.get_video_frames_generator(source)

        polygon_zone = sv.PolygonZone(SOURCE, frame_resolution_wh=self.video_info.resolution_wh)
        view_transformer = PerspectiveTransformer(SOURCE, TARGET)

        coordinates = defaultdict(lambda: deque(maxlen=self.video_info.fps))

        for frame in frame_generator:
            frame = cv2.resize(frame, (1080, 720))  # New size (width, height)

            result = self.model(frame)[0]
            detections = sv.Detections.from_ultralytics(result)

            detections = detections[polygon_zone.trigger(detections)]

            detections = byte_track.update_with_detections(detections=detections)  # bytetrack

            points = detections.get_anchors_coordinates(anchor=sv.Position.BOTTOM_CENTER)
            points = view_transformer.transform_points(points=points).astype(int)
            for tracker_id, [_, y] in zip(detections.tracker_id, points):
                coordinates[tracker_id].append(y)
            labels = []

            speed_estimation(detections, coordinates, self.video_info, labels)

            annotated_frame = frame.copy()
            annotated_frame = sv.draw_polygon(annotated_frame, SOURCE, color=sv.Color.red(), thickness=2)
            annotated_frame = trace_annotator.annotate(
                scene=annotated_frame, detections=detections
            )
            annotated_frame = bounding_box_annotator.annotate(scene=annotated_frame, detections=detections)
            annotated_frame = label_annotator.annotate(scene=annotated_frame, detections=detections, labels=labels)

            if display:
                cv2.imshow('frame', annotated_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()
        ret, jpeg = cv2.imencode('.jpg', annotated_frame)

        return jpeg.tobytes()


if __name__ == '__main__':
    model_path = "/home/ishwor/anaconda3/envs/fyp/lib/python3.10/site-packages/services/speed/resources/yolov8_vehicledetection/best.pt"
    # source="rtsp://ishwor:subedi@192.168.1.106:5555/h264_opus.sdp"
    source = "/home/ishwor/Desktop/dataset/vehicle/video/vehicle video/VID_20240207_135617.mp4"
    # source=0
    display = True
    speed_estimation_service = SpeedEstimationService(model_path, source)
    speed_estimation_service.video_process_supervision(source, display)