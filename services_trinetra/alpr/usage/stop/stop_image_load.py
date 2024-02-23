"""
Created By: ishwor subedi
Date: 2024-02-05
"""

from services.alpr.usage import image_load_logger

IMAGE_LOAD_LOGGER=image_load_logger()

def update_file(flag_path):
    try:
        with open(flag_path, 'w') as flag_file:
            flag_file.write('True')
    except Exception as e:
        IMAGE_LOAD_LOGGER.info(f"Error updating flag file: {e}")



if __name__ == '__main__':
    file_path = 'services_trinetra/alpr/resources/flag_check/start_load_status.txt'
    update_file(file_path)
