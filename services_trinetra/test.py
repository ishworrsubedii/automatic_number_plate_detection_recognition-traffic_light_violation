"""
Created By: ishwor subedi
Date: 2024-04-08
"""

import cv2
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image


class EmbossedNumberPlate:
    def __init__(self, det_model, recognition_model, cls_model_dir):
        """

       Args: det_model: path to the detection model
                recognition_model: path to the recognition model
                cls_model_dir: path to the classification model

        """

        self.ocr = PaddleOCR(det_model_dir=det_model, cls_model_dir=cls_model_dir,
                             rec_model_dir=recognition_model, lang="en", use_gpu=False)
        self.img = None
        self.font_path = "/home/ishwor/Desktop/alpr_speed_traffic/services_trinetra/alpr/resources/fonts/nepali.ttf"

    def detection_recognition(self, img):
        """
        Args: img: image array of the number plate extracted from the vehicle image

        Returns: boxes: list of bounding boxes of the recognized text
                    txts: list of recognized text
                    scores: list of scores of the recognized text

        """

        self.img = img
        try:
            result = self.ocr.ocr(self.img, cls=False)
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

    def draw_recognized_text(self, boxes, txts, scores):
        """
        Args: boxes: list of bounding boxes of the recognized text
            txts: list of recognized text
            scores: list of scores of the recognized text

        Return: recognized_text_image: image with recognized text drawn on it

        """

        img = draw_ocr(self.img, boxes, txts, scores, font_path=self.font_path)
        recognized_text_image = Image.fromarray(img)

        return recognized_text_image


if __name__ == '__main__':
    det_model = 'services_trinetra/alpr/resources/embossed/embossed_number_plate_recognition_model/det/'
    recognition_model = 'services_trinetra/alpr/resources/embossed/embossed_number_plate_recognition_model/rec/'
    cls_model_dir = 'services_trinetra/alpr/resources/embossed/embossed_number_plate_recognition_model/cls'
    embossed = EmbossedNumberPlate(det_model=det_model, recognition_model=recognition_model,
                                   cls_model_dir=cls_model_dir)
    img = "/home/ishwor/Pictures/Screenshots/Screenshot from 2023-08-28 11-41-41.png"
    img = cv2.imread(img)
    boxes, txts, scores = embossed.detection_recognition(
        img)
    img = embossed.draw_recognized_text(boxes, txts, scores)
    img.show()
