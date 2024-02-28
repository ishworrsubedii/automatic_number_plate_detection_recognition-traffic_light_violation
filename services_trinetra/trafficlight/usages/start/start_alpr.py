"""
Created By: ishwor subedi
Date: 2024-02-28
"""
from services_trinetra.alpr.usage.start.start_alpr import StartAlprExample

if __name__ == '__main__':
    det_model = 'services_trinetra/trafficlight/resources/paddleocr/Multilingual_PP-OCRv3_det_infer'
    recognition_model = 'services_trinetra/trafficlight/resources/paddleocr/custom_rec'
    rec_char_dict = 'services_trinetra/trafficlight/resources/paddleocr/devanagari_dict.txt'

    img = 'services_trinetra/trafficlight/resources/plate_detected'
    output_path = 'services_trinetra/trafficlight/output/paddleocr_output/paddleocr_rec_output'
    non_rec_output_path = "services_trinetra/trafficlight/output/paddleocr_output/paddleocr_non_rec_output"
    font_path = 'services_trinetra/trafficlight/resources/paddleocr/fonts/nepali.ttf'
    flag_path = 'services_trinetra/trafficlight/resources/flag_check/alpr_status'

    result_path = "services_trinetra/trafficlight/output/paddleocr_output/result.txt"
    recognized_images_file_path = "services_trinetra/trafficlight/output/paddleocr_output/recognized_images_paths.txt"
    non_recognized_images_file_path = "services_trinetra/trafficlight/output/paddleocr_output/non_recognized_images_paths.txt"

    start_alpr = StartAlprExample(det_model=det_model, recognition_model=recognition_model, rec_char_dict=rec_char_dict,
                                  detected_img_dir=img, output_path=output_path,
                                  non_rec_output_path=non_rec_output_path, flag_path=flag_path
                                  , result_file=result_path, recognized_images_file_path=recognized_images_file_path,
                                  non_recognized_images_file_path=non_recognized_images_file_path, font_path=font_path
                                  )
    start_alpr.create_stop_flag()
    results_generator = start_alpr.start_service()
