# Automatic License Plate Recognition (ALPR) System

The main goal of this project is to develop an automatic license plate recognition system that can detect and recognize
the license plate of a vehicle. The system is designed to be used in traffic monitoring systems, parking systems, and
other applications where license plate recognition is required.

### Features

- Number plate detection
- Number plate recognition
- Real-time number plate detection and recognition

### Future Work

- Improve the accuracy of number plate recognition by making large custom dataset and training the model using other
  ocr.
- Implement the system in real-time traffic monitoring systems and parking systems.

### Number plate detection

- Yolo v8 is used for number plate detection
- Paper: [YOLOv8:A COMPREHENSIVE REVIEW OF YOLO: FROM YOLOV1 TO
  YOLOV8 AND BEYOND](https://arxiv.org/pdf/2304.00501v1.pdf)
    - Dataset is collected from the youtube videos and custom captured images
        - **Dataset link:** https://www.kaggle.com/datasets/ishworsubedii/vehicle-number-plate-datasetnepal
            
### Number plate recognition

- For number plate recognition, I have proposed PaddleOCR. However, I have also tried different algorithms like MMOCR
  and CNN-based algorithms such as EfficientNet and ResNet50. Nonetheless, PaddleOCR is the best for faster inference.


- I have achieved quite good accuracy on number sequences and number plates whose fonts are similar to the training
  data. Additionally, I have gained good accuracy on embossed number plates.


- My proposed solution on number plate recognition for nepali number is good for ba__pa and numbers plates


- **Dataset for ocr** is made through the image concatenation and and using the different font with different colors and
  background and prepared around 100k dataset
    - Dataset Link: https://www.kaggle.com/datasets/ishworsubedii/alpr-v2/data


- **Dataset for CNNN based algorithms** like resnet50 efficientnet is made through the extracting each character from
  the
  number plate like this
    - Dataset Link: https://www.kaggle.com/datasets/ishworsubedii/nepalese-license-plate-character-dataset

### Usage

1. **Step 1:** This will start capturing the images from the camera ie. webcam ,ipcam, etc. and save the images in the
   rtsp
   directory.

   **Start**

    ```
    python3 services_trinetra/alpr/usage/start/start_image_capture.py
    ```

   **Stop**

    ```
    python3 services_trinetra/alpr/usage/start/start_image_capture.py
    ```
2. **Step 2:** This will start to detect the number plate from the images captured in the rtsp directory and save the
   detected number plate in the detected_number_plate directory.

   **Start**

    ```
    python3 services_trinetra/alpr/usage/start/start_image_load.py
    ```

   **Stop**

    ```
    python3 services_trinetra/alpr/usage/stop/stop_image_load.py
    ```
3. **Step 3:** This will start to recognize the information from the images captured in the number plate detected
   directory and save the images in paddleocr_rec_output and paddleocr_non_rec_output directory.

   **Start**

    ```
    python3 services_trinetra/alpr/usage/start/start_alpr.py
    ```

   **Stop**

    ```
    python3 services_trinetra/alpr/usage/stop/stop_alpr.py
    ```

### Results

<img alt="Image 1" src="/result_images/paddleocr_demo/2024-03-22_1.jpg"/>
<img alt="Image 2" src="/result_images/paddleocr_demo/2024-03-22_213.jpg"/>
<img alt="Image 3" src="/result_images/paddleocr_demo/2024-03-22_211.jpg"/>
<img alt="Image 4" src="/result_images/paddleocr_demo/2024-03-22_21.jpg"/>
<img alt="Image 5" src="/result_images/paddleocr_demo/2024-03-22_144.jpg"/>
<img alt="Image 6" src="/result_images/paddleocr_demo/2024-03-22_205.jpg"/>
<img alt="Image 7" src="/result_images/paddleocr_demo/2024-03-22_130.jpg"/>
<img alt="Image 8" src="/result_images/paddleocr_demo/2024-03-22_105.jpg"/>
<img alt="Image 9" src="/result_images/paddleocr_demo/2024-03-22_99.jpg"/>
