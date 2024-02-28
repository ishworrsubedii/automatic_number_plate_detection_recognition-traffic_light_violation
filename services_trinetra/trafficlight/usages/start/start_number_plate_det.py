"""
Created By: ishwor subedi
Date: 2024-02-28
"""
import time

from services_trinetra.alpr.usage.start.start_image_load import StartImageLoadExample

if __name__ == "__main__":
    flag_path = "services_trinetra/trafficlight/resources/flag_check/number_plate_status"
    image_dir = 'services_trinetra/trafficlight/output/vehicle_detection/detected'
    model_path = 'services_trinetra/alpr/resources/yolov8/nnpd.pt'
    image_save_dir = 'services_trinetra/trafficlight/resources/plate_detected'

    image_load_service = StartImageLoadExample(flag_path, image_dir, model_path, image_save_dir)
    image_load_service.create_stop_flag()
    image_load_service.start_service()
    time.sleep(1)
