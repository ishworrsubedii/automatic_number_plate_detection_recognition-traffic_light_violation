# Traffic Light Violation Detection

<img src="/results/traffic_light_demo.jpg">
<img src="/results/traffic_light2.png">

The main goal of this module is to develop an automatic traffic light violation detection system that can detect traffic
light violation If they violate the traffic light and cross the road while at a red light, then the system will capture
the
number plate of that vehicle, recognize that number, and save it in the database.

**Workflow**:(We need to place the CCTV in such a position so that it can detect the traffic light and the vehicle.
number plate))

- Detect the traffic light
    - If it is red, then it will make a polygon in the zebra crossing. We can make a custom polygon.
    - Activate a certain defined polygon in the frame, and if a vehicle appears in that polygon, then it will capture
      the
      number plate of that vehicle and save it in the directory.
    - The captured image is used for recognition using the same approach as the ALPR module.

### Features

- Traffic light detection
- Traffic light violation detection(red light, yellow light, green light)
- Number plate detection
- Number plate recognition

### Future Work

- Improve the accuracy of the vehicle detection in the same area and at the at the same angle from the camera.
- Implement the system in real-time traffic monitoring systems and parking systems if possible.

### Traffic Light Detection

For traffic light detection, I have used three different methods:

- Yolo v8(traffic light detection)
- Template Matching (We will provide the similar 3 images as of the traffic light and it will detect the traffic light)
    - **Here I have used the template matching technique.**

- Polygon detection (we will provide the polygon of the traffic light, and it will detect the traffic light)

### Vehicle Detection

- Vehicle detection is done using the Yolo v8 model.with the Cusom dataset, which was collected from the YouTube videos.
  and custom-captured images
    - **Dataset link:** https://www.kaggle.com/datasets/ishworsubedii/vehicles-dataset-nepal

### Number plate Detection and Recognition

You can refer to the alpr module for the number plate detection and recognition.
[Automatic License Plate Recognition](/services_trinetra/alpr/README.md)

### Usage

**Step 1:** This will start capturing the images from the camera, i.e., webcam, IPcam, etc., and save the images in the
directory.

**Start**

```angular2html
python3 services_trinetra/trafficlight/usages/start/start_image_capture_traffic_light.py

```

**Stop**

```angular2html
python3 services_trinetra/trafficlight/usages/start/start_image_capture_traffic_light.py


```

**Step2:** This will take those images and detect traffic lights. For that, we can use a different approach, i.e., a
template. matching,polygon, yolo, and save that image in the directory, and also detect the color of that red light
using the hsv color.
extraction and save the frame, which will contain the red light in the frame.

**Start**

```angular2html
python3 services_trinetra/trafficlight/usages/start/start_traffic_color_light_detection.py
```

**Stop**

```angular2html
python3 services_trinetra/trafficlight/usages/stop/stop_traffic_color_light_detection.py

```

**Step3:** This will make a polygon on the zebra crossing area, and if some vehicle is touched or inside the polygon,
then it will capture the image of that vehicle, save it in the directory, and delete the previous image.

**Start**

```angular2html
python3 services_trinetra/trafficlight/usages/start/start_vehicle_detection.py

```

**Stop**

```angular2html
python3 services_trinetra/trafficlight/usages/stop/stop_vehicle_detection.py

```

**Step4:** This process will detect the number plate from that vehicle extracted from the vehicle detection process and
save in another directory and delete those images that are already used or processed.

**Start**

```angular2html
python3 services_trinetra/trafficlight/usages/start/start_number_plate_detection.py

```

**Stop**

```angular2html

python3 services_trinetra/trafficlight/usages/stop/stop_number_plate_detection.py

```

**Step5:** This will recognize the number plate from the detected number plate and save the recognized number plate with
the recognized information in the image and the non-recognized images in another directory, and delete the processed
images from
the plate-detected directory.
**Start**

```angular2html
python3 services_trinetra/trafficlight/usages/start/start_alpr.py

```

**Stop**

```angular2html
python3 services_trinetra/trafficlight/usages/stop/stop_alpr.py

```

#### Thank you for reading the documentation. If you have any queries, please feel free to contact.

[Email](ishworr.subedi@gmail.com)

[Linkedin](https://www.linkedin.com/in/ishworrsubedii/)

    

