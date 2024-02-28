"""
Created By: ishwor subedi
Date: 2024-02-05
"""
import time
from paddleocr import PaddleOCR
from services.alpr.src.entity.service_config import RecognitionConfig
from PIL import Image


class PaddleocrService:
    def __init__(self, config: RecognitionConfig):
        """

        :param config:
        """
        self.ocr = PaddleOCR(det_model_dir=config.det_model, rec_model_dir=config.recognition_model,
                             rec_char_dict_path=config.rec_char_dict,
                             use_angle_cls=True, use_gpu=True)

    def detection_recognition_cls(self, img):
        """
        :param img:
        :return:
        """
        try:
            result = self.ocr.ocr(img, cls=False)
            print(result)

            for idx in range(len(result)):

                if result[idx] is None:
                    return [], [], []
                else:

                    result = result[0]
                    boxes = [line[0] for line in result]
                    txts = [line[1][0] for line in result]
                    scores = [line[1][1] for line in result]
                    return boxes, txts, scores

        except Exception as e:
            print(f"An error occurred: {e}")
            return [], [], []


if __name__ == '__main__':
    det_model = 'services/alpr/resources/paddleocr/Multilingual_PP-OCRv3_det_infer/'
    recognition_model = 'services/alpr/resources/paddleocr/custom_recog/'
    rec_char_dict = 'services/alpr/resources/paddleocr/devanagari_dict.txt'
    config = RecognitionConfig(det_model=det_model, recognition_model=recognition_model, rec_char_dict=rec_char_dict)
    paddle_ocr = PaddleocrService(config=config)
    paddle_ocr.detection_recognition_cls(
        img="/home/ishwor/anaconda3/envs/fyp/services/python3.10/site-packages/services/alpr/resources/plate_detected/23a.jpg")
