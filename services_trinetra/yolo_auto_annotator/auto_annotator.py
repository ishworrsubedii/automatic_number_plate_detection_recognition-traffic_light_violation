"""
Created By: ishwor subedi
Date: 2024-02-06
"""
from pathlib import Path

from ultralytics import SAM, YOLO


def auto_annotate(data, det_model="yolo_auto_annotator/resources/yolov8x.pt", device="", output_dir=None):
    """
    This function takes in the path to a directory containing images and automatically annotates the images using the
    :param data:  Path to the directory containing images
    :param det_model:  Path to the detection model (cpu,cuda)
    :param device:   Device to run the model on
    :param output_dir:  Path to the directory to save the annotated labels
    :return:
    """
    vehicle_classes = [9]  # Class IDs for 'bicycle', 'car', 'motorcycle', 'bus', 'truck'

    det_model = YOLO(det_model)

    data = Path(data)
    if not output_dir:
        output_dir = data.parent / f"{data.stem}_auto_annotate_labels"
    Path(output_dir).mkdir(exist_ok=True, parents=True)

    det_results = det_model(data, stream=True, device=device)
    for result in det_results:
        class_ids = result.boxes.cls.int().tolist()  # noqa
        vehicle_detections = [i for i, cls_id in enumerate(class_ids) if cls_id in vehicle_classes]

        if len(vehicle_detections):
            boxes = result.boxes.xyxy

            image_array = result.orig_img

            image_height, image_width, _ = image_array.shape
            with open(f"{Path(output_dir) / Path(result.path).stem}.txt", "w") as f:
                for i in vehicle_detections:
                    # Normalize the bounding box coordinates
                    x_min, y_min, x_max, y_max = boxes[i].tolist()
                    center_x = ((x_min + x_max) / 2) / image_width
                    center_y = ((y_min + y_max) / 2) / image_height
                    width = (x_max - x_min) / image_width
                    height = (y_max - y_min) / image_height

                    f.write(f"{class_ids[i]} {center_x} {center_y} {width} {height}\n")


if __name__ == '__main__':
    auto_annotate(data='/home/ishwor/Desktop/dataset/traffic_light/datasets/dataset/images/',
                  det_model='services/yolo_auto_annotator/resources/yolov8n.pt',
                  output_dir='/home/ishwor/Desktop/dataset/traffic_light/datasets/dataset/labels2/', device='cuda')
