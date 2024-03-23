<div style="border: 2px solid #333; padding: 20px; display: flex; align-items: center; justify-content: center;">
    <div style="text-align: center;">
        <img src="/results/trinetra.png" width="100" height="100" style="margin-right: 20px;">
        <h1 style="font-family: 'Roboto', sans-serif; font-size: 2.5em; color: #39FF14;">Trinetra</h1>
        <h6 style="font-family: 'Roboto', sans-serif; font-size: 0.8em; color: #e0e0e0;">- Let us be protected by the third eye!</h6>
        <h2 style="font-family: 'Roboto', sans-serif; font-size: 1.5em; color: #39FF14;">Automatic Number Plate Detection Recognition and Traffic Light Violation Detection</h2>
    </div>

</div>


<p style="color: white; font-weight: bold;">
Here, I have not provided the model that I have trained so that nobody can misuse it. If you want the model,
can contact me
at <a href="https://www.linkedin.com/in/ishworrsubedii/" style="color: #39FF14; font-weight: bold;">LinkedIn</a> or <a href="mailto:ishworr.subedi@gmail.com" style="color: #39FF14; font-weight: bold;">Email</a>
</p>

## Video Demonstration(Youtube)

**Automatic Number Plate Recognition**

[![Trinetra](https://i.ytimg.com/an_webp/Xz8ykJ1enbc/mqdefault_6s.webp?du=3000&sqp=CMSS-q8G&rs=AOn4CLCcr6HnWfnnb0eiodJKp8IHTomsiQ)](https://youtu.be/Xz8ykJ1enbc)

**Traffic Light Violation**

[![Traffic Light](https://i.ytimg.com/an_webp/QriQzJunH4U/mqdefault_6s.webp?du=3000&sqp=CMCa-q8G&rs=AOn4CLBVUCwnzjvG6i_yA9VekVGFjwMxug)](https://www.youtube.com/watch?v=QriQzJunH4U)

## Overview

This is the repository for the Trinetra project. Trinetra is a project that aims to provide a solution for traffic
automatic number plate recognition and the traffic light violation for the nepali number plates. The project is divided
into three parts: the backend, the frontend, and the services. The backend is
responsible for the database and the API. The frontend is responsible for the user interface. The services are
responsible for the machine learning models that are used to detect vehicles, number plates, speed, and traffic lights.

## Objectives

- To Automate the process of number plate detection and recognition.
- To Automate the process of traffic light violation detection.
- To Monitor the recognition of the number plate and traffic light violation detection in real time and store the data.
  in the database for future reference and further analysis.
- To provide a user-friendly interface for the user to interact with the system.
- To monitor the images of number plate recognitions and traffic light violations in real time.

## Features

- Number Plate Detection and Recognition
- Traffic Light Violation Detection
- Real-time monitoring of number plate recognition and traffic light violation detection
- user-friendly interface for the user to interact with the system.
- Search and filter the number plate recognition and traffic light violation detection data.
- Monitor the images of number plate recognitions and traffic light violations in real time.

## Technologies Used

For the backend, the following technologies are used:

- Python
- Django
- Django Rest Framework
- PostgreSQL
- JWT Authentication

For the frontend, the following technologies are used:

- React
- Material UI
- Axios
- Redux
- Different Chart Libraries

For the services, the following technologies are used:

- Python
- OpenCV
- YOLO
- OCR
- OOPs Concept
- Different Machine Learning Libraries
- CNN

## Services for Trinetra

<details>
<summary>Click to expand</summary>

### 1. Number Plate Detection and Recognition

- Number plate detection and recognition is the process of detecting the number plate of a vehicle and recognizing the
  characters on the number plate. The process involves the following steps:
    - Number Plate Detection
    - Number Plate Recognition

    - [ALPR](services_trinetra/alpr/README.md)

### 2. Traffic Light Violation Detection

- Traffic light violation detection is the process of detecting the violation of traffic lights by vehicles. The process
  involves the following steps:
    - Traffic Light Detection
    - Vehicle Detection
    - Traffic Light Violation Detection

    - [Traffic light violation](services_trinetra/trafficlight/README.md)

</details>

## How to Install

<details>
<summary>Click to expand</summary>

#### 1. Clone the repository

```bash
git clone https://github.com/ishworrsubedii/automatic_number_plate_detection_recognition-traffic_light_violation.git
````

#### 2. Create Environment

```bash
conda create -n trinetra python=3.10
````

#### 3. Install the requirements

```bash
pip install -r requirement
````

### Backend

For the backend, open the suitable IDE, i.e., Pycharm, and set up the Conda environment.

### Frontend

For frontend, open the suitable idea, i.e., vs. code, and open the frontend-trinetra directory.The requirements for the
frontend are:

- Node package manager needs to be installed in the system

```angular2html
npm install
```

To start the frontend, run the following command:

```angular2html
npm start 
```

To build the optimized version of the frontend, run the following command:

```angular2html
npm run build
```

### Services

#### 1. Setup

```angular2html
cd services_trinetra
```

```bash
setup.py install
```

Copy the package of the` anaconda/trinetra/dist/lib` and add it into the site-packages of the python environment

For alpr

Change the IP of ipcam inside backend_trinetra/alpr/alprservices.py to your IP.

For traffic lights

Change the IP of the ipcam inside backend_trinetra/trafficlight/trafficlightservices.py.

</details>

## Contributors

Contributors to the project are always welcome. You can contribute to the project by forking the repository and creating
a pull request. You can also create an issue if you find any bugs or have any suggestions for the project.

