import time

import cv2 as cv
import os
import threading
from services_trinetra.alpr.src.services.detection.vehicle_number_plate_detection import DetectionService
from services_trinetra.alpr.src.entity.service_config import DetectionConfig


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

        self.image_info_save = None

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

            self.image_info_save.join()
            print("Image loading thread stopped.")

    def detected_information_save(self, results):
        if results:
            for prediction in results:
                bboxes = prediction.boxes.xyxy

                for i, bbox in enumerate(bboxes):
                    multiple_plates = len(bboxes) > 1
                    try:
                        bbox = bbox.int().tolist()
                        x1, y1, x2, y2 = bbox
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
                    results = self.detection_service.detect_image(self.latest_image_path,
                                                                  confidence_threshold=0.5,
                                                                  nms_threshold=0.4)
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
