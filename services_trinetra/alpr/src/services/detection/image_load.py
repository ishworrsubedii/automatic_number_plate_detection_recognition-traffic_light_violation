import time

import cv2 as cv
import os
import threading
from services_trinetra.alpr.src.services.detection.vehicle_number_plate_detection import DetectionService
from services_trinetra.alpr.src.entity.service_config import DetectionConfig
from services_trinetra.alpr.src.utils.imageutils import otus_binarization


class ImageLoad:
    def __init__(self, image_dir, model_path, detected_image_save_dir):
        self.flag = False
        self.thread_running = False
        self.image_load = None
        self.image_path_img = image_dir
        self.latest_image_path = None
        self.modle_path = model_path
        config = DetectionConfig(model_path=self.modle_path)
        self.detection_service = DetectionService(config)
        self.detected_image_save_dir = detected_image_save_dir
        self.filename = None
        self.display = True

        self.image_info_save = None
        self.original_image = None
        self.bbox = None
        self.image_display_thread = None

    def start_load_image(self):
        """
        Start the image loading thread
        :return:
        """
        self.image_load = threading.Thread(target=self.image_list)

        self.image_info_save = threading.Thread(target=self.detected_information_save)

        self.image_load.start()

        self.thread_running = True

    def stop_load_image(self):
        if self.thread_running:
            self.thread_running = False

            self.image_load.join()
            print("Stopping the image loading thread...")

    def detected_information_save(self, results):
        if results:
            for prediction in results:
                bboxes = prediction.boxes.xyxy

                for i, bbox in enumerate(bboxes):
                    multiple_plates = len(bboxes) > 1
                    try:

                        original_image = prediction.orig_img
                        bbox = bbox.int().tolist()
                        x1, y1, x2, y2 = bbox

                        try:
                            if self.display:
                                cv.namedWindow('Licence Plate Detection', cv.WINDOW_NORMAL)
                                cv.putText(original_image, 'number_plate', (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX,
                                           0.9,
                                           (0, 0, 255), 2)
                                cv.rectangle(original_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                                cv.imshow('Licence Plate Detection', original_image)
                                if cv.waitKey(1) & 0xFF == ord('q'):
                                    return
                        except:
                            print("Error displaying images")

                        cropped = prediction.orig_img[y1:y2, x1:x2]

                        if multiple_plates:
                            filename = f'{self.filename}_plate_{i + 1}.jpg'
                        else:
                            filename = f'{self.filename}.jpg'

                        cv.imwrite(os.path.join(self.detected_image_save_dir, filename), cropped)

                    except:
                        print('No plate detected')

    def image_list(self):
        time.sleep(2)
        while self.thread_running:
            files = sorted(os.listdir(self.image_path_img))
            for self.filename in files:
                if not self.thread_running:
                    break

                image_path = os.path.join(self.image_path_img, self.filename)

                self.latest_image_path = image_path
                print("Processing:", self.latest_image_path)

                rd = cv.imread(self.latest_image_path)
                time.sleep(0.5)
                if rd is not None:
                    results = self.detection_service.detect_image(image=self.latest_image_path,
                                                                  confidence_threshold=0.5,
                                                                  nms_threshold=0.4, display=False)
                    cv.waitKey(3)
                    print('done')
                    os.remove(self.latest_image_path)
                    self.detected_information_save(results)
                else:
                    print('Image Loading Failed .......')


if __name__ == '__main__':
    image_dir = 'services_trinetra/alpr/resources/rtsp'
    model_path = 'services_trinetra/alpr/resources/yolov8/nnpd.pt'
    detected_image_save_dir = 'services_trinetra/alpr/resources/plate_detected/'
    image_load_start_stop = ImageLoad(image_dir, model_path, detected_image_save_dir)
    image_load_start_stop.start_load_image()
