"""
Created By: ishwor subedi
Date: 2024-02-28
"""


def stop_number_plate_detection(flag_path):
    try:
        with open(flag_path, 'w') as flag_file:
            flag_file.write('True')
    except Exception as e:
        print(f"Error updating flag file: {e}")


if __name__ == '__main__':
    file_path = 'services_trinetra/trafficlight/resources/flag_check/number_plate_status'
    stop_number_plate_detection(file_path)
