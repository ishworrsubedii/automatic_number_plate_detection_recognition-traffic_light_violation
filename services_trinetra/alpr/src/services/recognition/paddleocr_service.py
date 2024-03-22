"""
Created By: ishwor subedi
Date: 2024-02-05
"""
import time
from paddleocr import PaddleOCR
from services_trinetra.alpr.src.entity.service_config import RecognitionConfig
from PIL import Image


class PaddleocrService:
    def __init__(self, config: RecognitionConfig):
        """
        Initialize the paddleocr service
        :param config:  RecognitionConfig
        """
        self.ocr = PaddleOCR(det_model_dir=config.det_model, rec_model_dir=config.recognition_model,
                             rec_char_dict_path=config.rec_char_dict,
                             use_angle_cls=True, use_gpu=True)

    def detection_recognition_cls(self, img):
        """
        Detect and recognize the text from the image
        :param img: str
        :return:  bbox, txts, scores
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
    det_model = 'services_trinetra/alpr/resources/paddleocr/Multilingual_PP-OCRv3_det_infer/'
    recognition_model = 'services_trinetra/alpr/resources/paddleocr/custom_recog/'
    rec_char_dict = 'services_trinetra/alpr/resources/paddleocr/devanagari_dict.txt'
    config = RecognitionConfig(det_model=det_model, recognition_model=recognition_model, rec_char_dict=rec_char_dict)
    paddle_ocr = PaddleocrService(config=config)
    paddle_ocr.detection_recognition_cls(
        img="/img.jpg")
