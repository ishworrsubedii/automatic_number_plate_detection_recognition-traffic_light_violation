"""
Created By: ishwor subedi
Date: 2024-02-19
"""
import cv2
import numpy as np


def speed_estimation(detections, coordinates, video_info, labels):
    """
    Speed estimation service
    :param detections:
    :param coordinates:
    :param video_info:
    :param labels:
    :return: None
    """
    for tracker_id in detections.tracker_id:
        if len(coordinates[tracker_id]) < video_info.fps / 2:
            labels.append(f"#{tracker_id}")
        else:
            coordinate_start = coordinates[tracker_id][-1]
            coordinate_end = coordinates[tracker_id][0]
            distance = abs(coordinate_start - coordinate_end)
            time = len(coordinates[tracker_id]) / video_info.fps
            speed = distance / time * 3.6
            labels.append(f"#{tracker_id} {int(speed)} km/h")