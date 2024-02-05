"""
Created By: ishwor subedi
Date: 2024-02-05
"""
import os


def make_flag_true(flag_path):
    try:
        with open(flag_path, 'w') as flag_file:
            flag_file.write('True')
    except Exception as e:
        print(f"Error updating flag file: {e}")


if __name__ == '__main__':
    file_path = 'services/alpr/resources/flag_check/capture_status.txt'
    make_flag_true(file_path)
