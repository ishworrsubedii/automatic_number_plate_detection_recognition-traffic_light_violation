from django.db import models
from datetime import datetime


class ImageCaptureDatabase(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    stopped_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default="in_progress")

    def __str__(self):
        return f"ImageCapture ID: {self.id}"

    class Meta:
        db_table = 'image_capture'


class ImageLoadDatabase(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    stopped_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default="in_progress")

    def __str__(self):
        return f"ImageLoad ID: {self.id}"

    class Meta:
        db_table = 'image_load'


class ALPRDatabase(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    stopped_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default="in_progress")

    def __str__(self):
        return f"ALPR Detection ID: {self.id}"

    class Meta:
        db_table = 'alpr'


class ALPRecognitionDatabase(models.Model):
    detection_id = models.CharField(max_length=100)
    recognized_info = models.CharField(max_length=100)  # Removed comma
    accuracy = models.CharField(max_length=100)
    date = models.CharField(max_length=200)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"ALPR Recognition ID: {self.id}"

    class Meta:
        db_table = 'alpr_recognition'
