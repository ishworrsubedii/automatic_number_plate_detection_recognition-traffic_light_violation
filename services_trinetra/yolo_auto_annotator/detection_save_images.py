"""
Created By: ishwor subedi
Date: 2024-03-08
"""
from pathlib import Path

from ultralytics import YOLO


def detection_save_img(data, det_model="yolo_auto_annotator/resources/yolov8x.pt", device="", output_dir=None):
    """
    This function takes in the path to a directory containing images and automatically annotates the images using the
    :param data:  Path to the directory containing images
    :param det_model:  Path to the detection model (cpu,cuda)
    :param device:   Device to run the model on
    :param output_dir:  Path to the directory to save the annotated labels
    :return:
    """
    vehicle_classes = [2, 3, 5, 7]  # Class IDs for 'bicycle', 'car', 'motorcycle', 'bus', 'truck'

    det_model = YOLO(det_model)

    data = Path(data)
    if not output_dir:
        output_dir = data.parent / f"{data.stem}_auto_annotate_labels"
    Path(output_dir).mkdir(exist_ok=True, parents=True)

    det_results = det_model(data, stream=True, device=device)
    import cv2

    # ...

    for result in det_results:
        class_ids = result.boxes.cls.int().tolist()
        vehicle_detections = [i for i, cls_id in enumerate(class_ids) if cls_id in vehicle_classes]

        if len(vehicle_detections):
            boxes = result.boxes.xyxy

            image_array = result.orig_img

            image_height, image_width, _ = image_array.shape
            for i in vehicle_detections:
                x_min, y_min, x_max, y_max = boxes[i].tolist()

                # Crop the detected part and save it as an image
                crop_img = image_array[int(y_min):int(y_max), int(x_min):int(x_max)]
                cv2.imwrite(f"{Path(output_dir) / Path(result.path).stem}_{i}.jpg", crop_img)
                print(f"{Path(output_dir) / Path(result.path).stem}_{i}.jpg")


if __name__ == '__main__':
    detection_save_img(data='/home/ishwor/Desktop/dataset/img/',
                       det_model='services_trinetra/yolo_auto_annotator/resources/yolov8s.pt',
                       output_dir='/home/ishwor/Desktop/dataset/vehicle_extracted/',
                       device='cuda')
