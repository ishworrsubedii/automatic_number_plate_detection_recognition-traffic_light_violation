"""
Created By: ishwor subedi
Date: 2024-03-04
"""
import os
from datetime import datetime

def rename_images(directory):
    date_today = datetime.today().strftime('%Y-%m-%d')
    counter = 1

    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            new_filename = f"{date_today}_{counter}{os.path.splitext(filename)[1]}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            counter += 1


if __name__ == '__main__':
    # Example usage
    directory = "/home/ishwor/Music/test_datasets/images/"
    rename_images(directory)
