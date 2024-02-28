"""
Created By: ishwor subedi
Date: 2024-02-29
"""
from rest_framework import serializers
from .models import (
    ImageCaptureDatabaseTrafficLight,
    TrafficlightColorDetectionTrafficlight,
    VehicleDetectionTrafficLight,
    NumberPlateDetectionTrafficLight,
    NumberPlateRecognitionTrafficLight,
    RedLightViolatedVehiclesListTrafficLight,
    VehicleNotDetectedImageListDatabaseTrafficLight,
    ALPRRecognitionResultDatabaseTrafficLight,
    ALPRRecognizedImageDatabaseTrafficLight,
    ALPRNonRecognizedImageDatabaseTrafficLight,
)


class ImageCaptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCaptureDatabaseTrafficLight
        fields = ['id', 'started_at', 'stopped_at', 'status']


class TrafficlightColorDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficlightColorDetectionTrafficlight
        fields = ['id', 'started_at', 'stopped_at', 'status']


class VehicleDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetectionTrafficLight
        fields = ['id', 'started_at', 'stopped_at', 'status']


class NumberPlateDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberPlateDetectionTrafficLight
        fields = ['id', 'started_at', 'stopped_at', 'status']


class NumberPlateRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberPlateRecognitionTrafficLight
        fields = ['id', 'started_at', 'stopped_at', 'status']


class RedLightViolatedVehiclesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedLightViolatedVehiclesListTrafficLight
        fields = ['id', 'traffic_light_violated_images']


class VehicleNotDetectedImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleNotDetectedImageListDatabaseTrafficLight
        fields = ['id', 'vehicle_not_detected_images']


class ALPRRecognitionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALPRRecognitionResultDatabaseTrafficLight
        fields = ['id', 'violation_id', 'image_path', 'recognized_info', 'accuracy', 'date', 'violation_type', 'status']


class ALPRRecognizedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALPRRecognizedImageDatabaseTrafficLight
        fields = ['id', 'recognized_image_path']


class ALPRNonRecognizedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALPRNonRecognizedImageDatabaseTrafficLight
        fields = ['id', 'non_recognized_image_path']
