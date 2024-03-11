"""
Created By: ishwor subedi
Date: 2024-03-03
"""
import cv2
from paddleocr import PaddleOCR

from services_trinetra.alpr.src.entity.service_config import EmbossedNumberPlateConfig

from paddleocr import PaddleOCR, draw_ocr
from services_trinetra.alpr.src.utils.imageutils import otus_binarization


class EmbossedNumberPlate:
    def __init__(self, config: EmbossedNumberPlateConfig):
        """
        Initialize the paddleocr model

        """

        self.ocr = PaddleOCR(det_model_dir=config.det_model, cls_model_dir=config.cls_model_dir,
                             rec_model_dir=config.recognition_model, lang="en",

                             use_gpu=True)

    def detection_recognition_cls(self, img):
        """
         recognize the text from the image
        :param img:  image path
        :return:  boxes, txts, scores
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
    det_model = 'services_trinetra/alpr/resources/embossed/embossed_number_plate_recognition_model/det/'
    recognition_model = 'services_trinetra/alpr/resources/embossed/embossed_number_plate_recognition_model/rec/'
    cls_model_dir = 'services_trinetra/alpr/resources/embossed/embossed_number_plate_recognition_model/cls'
    char_dict = 'services_trinetra/alpr/resources/paddleocr/en_dict.txt'
    config = EmbossedNumberPlateConfig(det_model=det_model, recognition_model=recognition_model,
                                       cls_model_dir=cls_model_dir, char_dict=char_dict
                                       )
    paddle_ocr = EmbossedNumberPlate(config=config)
    paddle_ocr.detection_recognition_cls(
        img="services_trinetra/alpr/resources/embossed/embossed_images/em.png")
