"""
Created By: ishwor subedi
Date: 2024-02-05
"""
import time
from paddleocr import PaddleOCR
from services.alpr.src.entity.service_config import RecognitionConfig


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

        start_time = time.time()
        result = self.ocr.ocr(img, cls=False)
        stop_time = time.time()
        try:
            for idx in range(len(result)):
                res = result[idx]
                for line in res:
                    print(line)

            result = result[0]
            boxes = [line[0] for line in result]
            txts = [line[1][0] for line in result]
            scores = [line[1][1] for line in result]
            execution_time = stop_time - start_time
            return boxes, txts, scores
        except:
            print('Nothing recognized...')
