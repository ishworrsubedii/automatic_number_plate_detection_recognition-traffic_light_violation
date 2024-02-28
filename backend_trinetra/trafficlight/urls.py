"""
Created By: ishwor subedi
Date: 2024-02-28
"""
from django.urls import path
from .views import (ImageCaptureStartView, ImageCaptureStopView,
                    TrafficLightColorDetectionStartView, TrafficLightColorDetectionStopView,
                    VehicleDetectionPolygonStartView, VehicleDetectionPolygonStopView,
                    NumberPlateDetectionStartView, NumberPlateDetectionStopView,
                    AutomaticNumberPlateRecogniztionStartView, AutomaticNumberPlateRecogniztionStopView,
                    CaptureStatusView, ColorDetectionStatusView, VehicleDetectionStatusView,
                    NumberPlateDetectionStatusView, NumberPlateRecognitionStatusView, RedLightViolatedVehiclesListView,
                    VehicleNotDetectedImageView, ALPRRecognitionResultView, ALPRRecognizedImageView,
                    ALPRNonRecognizedImageView)

urlpatterns = [
    path('image_capture/start/', ImageCaptureStartView.as_view(), name='image_capture_start'),
    path('image_capture/stop/', ImageCaptureStopView.as_view(), name='image_capture_stop'),
    path('traffic_light_color_detection/start/', TrafficLightColorDetectionStartView.as_view(),
         name='traffic_light_color_detection_start'),
    path('traffic_light_color_detection/stop/', TrafficLightColorDetectionStopView.as_view(),
         name='traffic_light_color_detection_stop'),
    path('vehicle_detection/start/', VehicleDetectionPolygonStartView.as_view(),
         name='vehicle_detection_start'),
    path('vehicle_detection/stop/', VehicleDetectionPolygonStopView.as_view(),
         name='vehicle_detection_stop'),
    path('number_plate_detection/start/', NumberPlateDetectionStartView.as_view(),
         name='number_plate_detection_start'),
    path('number_plate_detection/stop/', NumberPlateDetectionStopView.as_view(),
         name='number_plate_detection_stop'),
    path('alpr/start/', AutomaticNumberPlateRecogniztionStartView.as_view(),
         name='alpr_start'),
    path('alpr/stop/', AutomaticNumberPlateRecogniztionStopView.as_view(),
         name='alpr_stop'),

    # get requests

    path('capture-status/', CaptureStatusView.as_view(), name='capture-status'),
    path('color-detection-status/', ColorDetectionStatusView.as_view(), name='color-detection-status'),
    path('vehicle-detection-status/', VehicleDetectionStatusView.as_view(), name='vehicle-detection-status'),
    path('number-plate-detection-status/', NumberPlateDetectionStatusView.as_view(),
         name='number-plate-detection-status'),
    path('number-plate-recognition-status/', NumberPlateRecognitionStatusView.as_view(),
         name='number-plate-recognition-status'),
    path('red-light-violated-vehicles-list/', RedLightViolatedVehiclesListView.as_view(),
         name='red-light-violated-vehicles-list'),
    path('vehicle-not-detected-image-list/', VehicleNotDetectedImageView.as_view(),
         name='vehicle-not-detected-image-list'),
    path('alpr-recognition-result/', ALPRRecognitionResultView.as_view(), name='alpr-recognition-result'),
    path('alpr-recognized-images/', ALPRRecognizedImageView.as_view(), name='alpr-recognized-images'),
    path('alpr-non-recognized-images/', ALPRNonRecognizedImageView.as_view(), name='alpr-non-recognized-images'),

]
