"""
Created By: ishwor subedi
Date: 2024-02-19
"""
import supervision as sv

def object_tracking(video_info):
    """
     Object tracking service
    :param video_info:  video information
    :return:  byte_track
    """
    byte_track = sv.ByteTrack(frame_rate=video_info.fps)  # bytetrack
    return byte_track
