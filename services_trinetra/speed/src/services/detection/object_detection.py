"""
Created By: ishwor subedi
Date: 2024-02-19
"""

import numpy as np
from ultralytics import YOLO
import supervision as sv
import cv2



class PerspectiveTransformer:
    def __init__(self, source, target):
        """

        :param source:
        :param target:
        """
        source = source.astype(np.float32)
        target = target.astype(np.float32)
        self.m = cv2.getPerspectiveTransform(source, target)

    def transform_points(self, points):
        """

        :param points:
        :return:
        """
        if points.size == 0:
            return points

        reshaped_points = points.reshape(-1, 1, 2).astype(np.float32)
        transformed_points = cv2.perspectiveTransform(reshaped_points, self.m)
        return transformed_points.reshape(-1, 2)


class ObjectDetectionService:
    def __init__(self, model_path, source):
        """
        Object detection service
        :param model_path:  model path
        :param source:  source
        """
        self.model = YOLO(model_path)
        self.\
            video_info = sv.VideoInfo.from_video_path(video_path=source)