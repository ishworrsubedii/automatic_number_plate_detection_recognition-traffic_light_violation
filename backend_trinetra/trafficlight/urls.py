"""
Created By: ishwor subedi
Date: 2024-02-28
"""
from django.urls import path
from .views import (ImageCaptureStartView, ImageCaptureStopView,
                    TrafficLightColorDetectionStartView, TrafficLightColorDetectionStopView,
                    VehicleDetectionPolygonStartView, VehicleDetectionPolygonStopView,
                    NumberPlateDetectionStartView, NumberPlateDetectionStopView,
                    AutomaticNumberPlateRecogniztionStartView, AutomaticNumberPlateRecogniztionStopView)

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

]
