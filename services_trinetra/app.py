import tempfile
import PIL
import streamlit as st
from paddleocr import PaddleOCR, draw_ocr
from ultralytics import YOLO
import json
import matplotlib.pyplot as plt
import cv2
import matplotlib.patches as patches
import numpy as np
from PIL import Image
import paddleocr
from test import EmbossedNumberPlate

class LicensePlateApp:
    def __init__(self):
        self.model = YOLO('/home/ishwor/Desktop/alpr_speed_traffic/services_trinetra/alpr/resources/yolov8/nnpd.pt')
        self.c_detector = YOLO('/home/ishwor/Desktop/alpr_speed_traffic/services_trinetra/alpr/resources/yolov8/best.pt')

    def heading(self):
        st.set_page_config(page_title='AI Based License Plate Detection',
                           page_icon="🚗", )

        st.markdown('''
          <style>
            @import url('https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,100..900;1,100..900&display=swap')
            @import url('https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,100..900;1,100..900&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap')
            @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&display=swap')
          </style>
        ''', unsafe_allow_html=True)

        st.title('AI Based License Plate Detection System')
        st.markdown('''
          <h2 style="font-family: 'DM Serif Display', serif; font-size: 1.3rem;
                    font-style: italic;">
            by Sarthak Shrestha
          </h2>
        ''', unsafe_allow_html=True)
        st.markdown(
            'This web-app was created for my Final Year Project where I have developed a license plate detector through deep learning which falls under the big compass of Artificial Intelligence')
        st.info("Hit the top left sidebar button to get started!")

        st.divider()

        st.divider()

    def maintain_aspect_ratio(self, image_path, max_width=350):
        image = PIL.Image.open(image_path)
        width, height = 700, 700
        new_height = int(max_width * (height / float(width)))
        resized_image = image.resize((max_width, new_height))
        return resized_image

    def embossed_number_plate(self, roi):
        det_model = 'alpr/resources/embossed/embossed_number_plate_recognition_model/det/'
        recognition_model = 'alpr/resources/embossed/embossed_number_plate_recognition_model/rec/'
        cls_model_dir = 'alpr/resources/embossed/embossed_number_plate_recognition_model/cls'
        embossed = EmbossedNumberPlate(det_model=det_model, recognition_model=recognition_model,
                                       cls_model_dir=cls_model_dir)
        boxes, txts, scores = embossed.detection_recognition(
            roi)
        img = embossed.draw_recognized_text(boxes, txts, scores)

        return img

    def display_image_with_boxes(self, image, results):
        fig, ax = plt.subplots(1)
        ax.imshow(image)

        for result in results:
            box = result['box']
            rect = patches.Rectangle((box['x1'], box['y1']),
                                     box['x2'] - box['x1'],
                                     box['y2'] - box['y1'],
                                     linewidth=1, edgecolor='w', facecolor='none')

            ax.add_patch(rect)
            confidence_percent = result['confidence'] * 100
            plt.text(box['x1'], box['y1'] - 10,
                     f"{result['name']} ({confidence_percent:.2f}%)", color='w', weight='bold', fontsize=9)

        plt.axis('off')
        return fig

    def display_characters(self, image, confidence_of_character):
        fig, ax = plt.subplots(1)
        ax.imshow(image)
        results = self.c_detector(image, conf=confidence_of_character)  # Call model directly with image data
        results = json.loads(results[0].tojson())
        predicted_characters = []
        for result in results:
            predicted_characters.append(result['name'])
            box = result['box']
            rect = patches.Rectangle((box['x1'], box['y1']),
                                     box['x2'] - box['x1'],
                                     box['y2'] - box['y1'],
                                     linewidth=1, edgecolor='w', facecolor='none')
            ax.add_patch(rect)
            plt.text(box['x1'], box['y1'] - 10, f"{result['name']}", color='w', weight='bold', fontsize=12)

        plt.axis('off')
        return predicted_characters, fig

    def run(self):
        self.heading()
        col1, col2 = st.columns(2)
        with st.sidebar:
            st.title('1. Input image for detection')
            st.subheader('**Upload Image**')
            source_image = st.file_uploader("Upload a png/jpeg file containing license plate to detect",
                                            type=("jpg", "jpeg", "png", 'bmp', 'webp'))
            with col1:
                if source_image:
                    uploaded_image = PIL.Image.open(source_image)
                    image_width, image_height = uploaded_image.size
                    st.image(source_image,
                             caption="Uploaded Image for License Detection",
                             use_column_width="auto")

            st.title('2. Set Confidence of License Plate Detection')
            confidence = float(st.slider(
                "Select Model Confidence", 25, 100, 40)) / 100

            st.header('3. Set Confidence of Character Recognition within License Plate')
            confidence_of_character = float(st.slider(
                "Select Model Confidence", 25, 100, 40,
                key="character_confidence")) / 100

            if st.sidebar.button('Detect License Plate & Characters'):
                image_bytes = source_image.read()
                image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = self.model(uploaded_image, conf=confidence)
                results = json.loads(results[0].tojson())
                fig = self.display_image_with_boxes(image, results)

                with col1:
                    st.markdown("Detected License plate from the uploaded image:")
                    fig = self.display_image_with_boxes(image, results)
                    st.pyplot(fig, use_container_width=True)

                with col2:
                    for i, result in enumerate(results):
                        box = result['box']
                        roi = image[int(box['y1']):int(box['y2']), int(box['x1']):int(box['x2'])]
                        predicted_characters, character_image = self.display_characters(roi, confidence_of_character)
                        confidence = result['confidence'] * 100
                        col1, col2 = st.columns(2)
                        fig, ax = plt.subplots()
                        ax.imshow(roi)
                        ax.axis('off')
                        with col1:
                            st.pyplot(fig, use_container_width=True)
                            st.markdown(f"License Plate (ROI) # {i + 1}: `{result['name']} ({confidence:.2f}%)`")
                            st.divider()

                        with col2:
                            st.pyplot(character_image, use_container_width=True)
                            st.markdown(
                                f"Predicted Characters: {i + 1} \n: `{' '.join(predicted_characters)} ({confidence:.2f}%)`")

                    st.markdown('**License Plates detected from the uploaded images**')

            if st.sidebar.button("Detect Embossed Number Plate"):
                image_bytes = source_image.read()
                image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = self.model(uploaded_image, conf=confidence)
                results = json.loads(results[0].tojson())
                fig = self.display_image_with_boxes(image, results)

                with col1:
                    st.markdown("Detected License plate from the uploaded image:")
                    fig = self.display_image_with_boxes(image, results)
                    st.pyplot(fig, use_container_width=True)

                with col2:
                    for i, result in enumerate(results):
                        box = result['box']
                        roi = image[int(box['y1']):int(box['y2']), int(box['x1']):int(box['x2'])]
                        img = self.embossed_number_plate(roi)
                        col1, col2 = st.columns(2)
                        fig, ax = plt.subplots()
                        ax.imshow(img)
                        ax.axis('off')
                        with col1:
                            st.pyplot(fig, use_container_width=True)
                            st.markdown(f"License Plate (ROI) # {i + 1}: `{result['name']} ({confidence:.2f}%)`")
                            st.divider()

                        with col2:
                            st.pyplot(img, use_column_width=True)

        st.title('License Plate Detection Model')
        st.divider()
        st.subheader('Benchmark of License Plate Detection from Custom Dataset from training with YOLOv8')
        st.markdown('Precision: **86.7%**')
        st.markdown('Mean Average Precision : **93.2%**')
        st.markdown('Mean Average Precision (50 - Threshold): **95.7%**')
        st.markdown('Epoch count: **50**')
        st.markdown('F1 Score: (Mean of Precision and Reacall at 45.8% confidence): **93%**')
        st.divider()

        st.subheader("Dataset detail of License Plate Detection model")
        col = st.columns(4)
        col[0].metric(label="No. of total images", value=1677, delta="")
        col[1].metric(label="No. of training images", value=1172, delta="")
        col[2].metric(label="No. of valid images", value=333, delta="")
        col[3].metric(label="No. of testing images", value=172, delta="")
        st.divider()

        st.subheader("Graphs of License Plate Detection Model :chart_with_upwards_trend:")
        st.text("Performance Metric Images of the License Plate Model")
        col1, col2 = st.columns(2)

        with col1:
            col1.image('lp-model-images/labels.jpg', caption='Label Graph - Single Label', use_column_width=True)
            col1.image('lp-model-images/labels_correlogram.jpg', caption="Correlogram of License Plate Detection Model",
                       use_column_width=True)
            col1.image('lp-model-images/confusion_matrix_normalized.png', caption='Normalized Confusion Matrix',
                       use_column_width=True)
            col1.image('lp-model-images/train_batch0.jpg', caption='Training Batch 0', use_column_width=True)

        with col2:
            image_path1 = 'lp-model-images/PR_curve1.png'
            image1 = Image.open('lp-model-images/PR_curve1.png')
            resized_image1 = image1.resize((350, 350))
            resized_image = self.maintain_aspect_ratio(image_path1)
            st.image(resized_image, caption='Precision recall curve')

            image2 = Image.open('lp-model-images/F1_curve.png')
            resized_image2 = image2.resize((350, 350))
            col2.image(resized_image2, caption='F1 Score curve')

            col2.image('lp-model-images/confusion_matrix.png', caption='Confusion Matrix', use_column_width=True)

            image3 = Image.open('lp-model-images/P_curve.png')
            resized_image3 = image3.resize((350, 350))
            col2.image(resized_image3, caption='Precision Confidence Curve')
        st.subheader('Overview of the License Plate Detection Model')
        st.image('lp-model-images/results.png', caption='Overview of the License Plate Detection Model', use_column_width=True)
        st.divider()

        st.title('Character Recognition within License Plate Model')
        st.divider()
        st.subheader('Benchmark of Character Recognition within License Plates from Custom Dataset trained from YOLOv8')
        st.markdown('Precision: **95%**')
        st.markdown('Mean Average Precision: **89.3%**')
        st.markdown('Mean Average Precision (50 - Threshold): **89.3%**')
        st.markdown('Epoch count: **50**')
        st.markdown('F1 Score: (Mean of Precision and Reacall at 31.4% confidence for all classes): **85%** ')
        st.divider()

        st.subheader("Dataset detail of Character Recognition model")
        col = st.columns(4)
        col[0].metric(label="No. of total images", value=597, delta="")
        col[1].metric(label="No. of training images", value=419, delta="")
        col[2].metric(label="No. of valid images", value=118, delta="")
        col[3].metric(label="No. of testing images", value=60, delta="")
        st.divider()

        st.subheader("Graphs of Character Recognition within License Plate Model :chart_with_upwards_trend:")
        st.text("Performance Metric Images of the Character Recognition Model")
        col1, col2 = st.columns(2)

        with col1:
            st.image('character-model-images/labels.jpg', caption='Label Graph - Multiple Labels', width=400,
                     use_column_width=True)
            st.image('character-model-images/labels_correlogram.jpg', caption="Correlogram of Character Recognition Model",
                     width=400, use_column_width=True)
            st.image('character-model-images/confusion_matrix_normalized.png', caption='Normalized Confusion Matrix', width=400,
                     use_column_width=True)
            st.image('character-model-images/train_batch0.jpg', caption='Training Batch 0', width=400, use_column_width=True)

        with col2:
            image_path3 = 'character-model-images/PR_curve.png'
            resized3 = self.maintain_aspect_ratio(image_path3)
            st.image(resized3, caption='Precision recall curve @ 0.5')

            image_path4 = 'character-model-images/F1_curve.png'
            resized4 = self.maintain_aspect_ratio(image_path4)
            st.image(resized4, caption='F1 Score curve')

            st.image('character-model-images/confusion_matrix.png', caption='Confusion Matrix', width=400,
                     use_column_width=True)

            image_path5 = 'character-model-images/P_curve.png'
            resized5 = self.maintain_aspect_ratio(image_path5)
            st.image(resized5, caption='Precision Confidence curve')

        st.subheader('Overview of the Character Recognition Model')
        st.image('character-model-images/results.png', caption='Overview of the Character Recognition Model',
                 use_column_width=True)

        st.divider()
        st.markdown('Developed thoroughly through `YOLOv8, Roboflow and Python`')

if __name__ == "__main__":
    app = LicensePlateApp()
    app.run()