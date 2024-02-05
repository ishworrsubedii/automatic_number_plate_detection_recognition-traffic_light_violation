"""
Created By: ishwor subedi
Date: 2024-02-05
"""
import os
from datetime import datetime

from PIL.Image import Image
from paddleocr.tools.infer.utility import draw_ocr

from services.alpr.src.services.recognition.paddleocr_service import PaddleocrService
from services.alpr.src.entity.service_config import RecognitionConfig


def service_example(det_model, recognition_model, rec_char_dict, img):
    config = RecognitionConfig(det_model=det_model, recognition_model=recognition_model, rec_char_dict=rec_char_dict,
                               )
    paddle_ocr = PaddleocrService(config)
    boxes, txts, scores = paddle_ocr.detection_recognition_cls(img)

    return boxes, txts, scores


if __name__ == '__main__':
    det_model = 'services/alpr/resources/paddleocr/Multilingual_PP-OCRv3_det_infer/'
    recognition_model = 'services/alpr/resources/paddleocr/custom_recog/'
    rec_char_dict = 'services/alpr/resources/paddleocr/devanagari_dict.txt'

    img = 'services/alpr/resources/plate_detected/0a.jpg.jpg'
    output_path = 'services/alpr/resources/images/paddleocr_output/'
    font_path = 'services/alpr/resources/fonts/nepali.ttf'
    boxes, txts, scores = service_example(det_model, recognition_model, rec_char_dict, img)
    print(boxes, txts, scores)
