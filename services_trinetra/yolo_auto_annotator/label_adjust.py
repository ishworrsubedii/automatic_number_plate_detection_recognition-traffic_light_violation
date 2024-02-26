"""
Created By: ishwor subedi
Date: 2024-02-21
"""
import os
import glob


def edit_first_number_in_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        line = lines[i].split()
        if line:  # Check if line is not empty
            line[0] = '0'
            lines[i] = ' '.join(line) + '\n'

    with open(file, 'w') as f:
        f.writelines(lines)


def process_files(directory):
    txt_files = glob.glob(os.path.join(directory, '*.txt'))

    for file in txt_files:
        edit_first_number_in_file(file)


if __name__ == '__main__':
    directory_path = "dataset/traffic_light/datasets/dataset/labels2/"
    process_files(directory_path)
