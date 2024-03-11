"""
Created By: ishwor subedi
Date: 2024-02-05
"""
import os
from datetime import datetime

from PIL.Image import Image
from paddleocr.tools.infer.utility import draw_ocr

from services_trinetra.alpr.src.services.recognition.paddleocr_service import PaddleocrService
from services_trinetra.alpr.src.entity.service_config import RecognitionConfig


def service_example(det_model, recognition_model, rec_char_dict, img):
    config = RecognitionConfig(det_model=det_model, recognition_model=recognition_model, rec_char_dict=rec_char_dict,
                               )
    paddle_ocr = PaddleocrService(config)
    boxes, txts, scores = paddle_ocr.detection_recognition_cls(img)

    return boxes, txts, scores


if __name__ == '__main__':
    det_model = 'services_trinetra/alpr/resources/paddleocr/dett/Multilingual_PP-OCRv3_det_infer'
    # recognition_model = 'services_trinetra/alpr/resources/paddleocr/custom_recog/'

    recognition_model = 'services_trinetra/alpr/resources/paddleocr/final_model_rec/'
    rec_char_dict = 'services_trinetra/alpr/resources/paddleocr/en_dict.txt'

    img = '/home/ishwor/Desktop/TreeLeaf/Vehicle Number Plate/Dataset/images/8a.jpg'
    output_path = 'services_trinetra/alpr/resources/images/paddleocr_rec_output/'
    font_path = 'services_trinetra/alpr/resources/fonts/nepali.ttf'
    boxes, txts, scores = service_example(det_model, recognition_model, rec_char_dict, img)
    print(boxes, txts, scores)
