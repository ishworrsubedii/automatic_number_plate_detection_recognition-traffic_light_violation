"""
Created By: ishwor subedi
Date: 2024-02-23
"""
from rest_framework import serializers
from .models import ALPRecognitionDatabase, ALPRRecognizedImageDatabase, ALPRNonRecognizedImageDatabase


class ALPRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALPRecognitionDatabase
        fields = ['id', 'detection_id', 'image_path', 'recognized_info', 'accuracy', 'date', 'status']


class AlPRecogniizedImagePathsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALPRRecognizedImageDatabase
        fields = ['id', 'recognized_image_path']


class AlPNonRecogniizedImagePathsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALPRNonRecognizedImageDatabase
        fields = ['id', 'non_recognized_image_path']
