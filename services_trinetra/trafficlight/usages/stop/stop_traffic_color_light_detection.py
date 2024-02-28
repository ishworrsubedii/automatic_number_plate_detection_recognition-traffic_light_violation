"""
Created By: ishwor subedi
Date: 2024-02-27
"""
"""
Created By: ishwor subedi
Date: 2024-02-05
"""


def stop_traffic_color_light_detection(flag_path):
    try:
        with open(flag_path, 'w') as flag_file:
            flag_file.write('True')
    except Exception as e:
        print(f"Error updating flag file: {e}")



if __name__ == '__main__':
    file_path = 'services_trinetra/trafficlight/resources/flag_check/traffic_light.txt'
    stop_traffic_color_light_detection(file_path)
