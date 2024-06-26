from django.db import models


# Databse for storing status of services
class ImageCaptureDatabaseTrafficLight(models.Model):
    """
    This model is used to store the status of the image capture service.
    """
    started_at = models.DateTimeField(auto_now_add=True)
    stopped_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default="in_progress")

    def __str__(self):
        return f"ImageCapture ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_image_capture_status'


class TrafficlightColorDetectionTrafficlight(models.Model):
    """
    This model is used to store the status of the traffic light color detection service.
    """
    started_at = models.DateTimeField(auto_now_add=True)
    stopped_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default="in_progress")

    def __str__(self):
        return f"TrafficlightColorDetection ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_color_detection_status'


class VehicleDetectionTrafficLight(models.Model):
    """
    This model is used to store the status of the vehicle detection service.
    """
    started_at = models.DateTimeField(auto_now_add=True)
    stopped_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default="in_progress")

    def __str__(self):
        return f"VehicleDetection ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_vehicle_detection_status'


class NumberPlateDetectionTrafficLight(models.Model):
    """
    This model is used to store the status of the number plate detection service.
    """
    started_at = models.DateTimeField(auto_now_add=True)
    stopped_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default="in_progress")

    def __str__(self):
        return f"NumberPlateDetection ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_number_plate_detection_status'


class NumberPlateRecognitionTrafficLight(models.Model):
    """
    This model is used to store the status of the number plate recognition service.
    """
    started_at = models.DateTimeField(auto_now_add=True)
    stopped_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default="in_progress")

    def __str__(self):
        return f"NumberPlateRecognition ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_number_plate_recognition_status'


class RedLightViolatedVehiclesListTrafficLight(models.Model):
    """
    This model is used to store the list of vehicles that violated the red light.
    """
    traffic_light_violated_images = models.CharField(max_length=500)

    def __str__(self):
        return f"RedLightViolatedVehiclesList ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_red_light_violated_vehicles_list'


class VehicleNotDetectedImageListDatabaseTrafficLight(models.Model):
    """
    This model is used to store the list of images where the vehicle is not detected.
    """
    vehicle_not_detected_images = models.CharField(max_length=500)

    def __str__(self):
        return f"VehicleNotDetectedImageList ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_vehicle_not_detected_image_list'


# Database for storing recognized result
class ALPRRecognitionResultDatabaseTrafficLight(models.Model):
    """
    This model is used to store the result of the ALPR recognition service.
    """
    violation_id = models.CharField(max_length=100)
    image_path = models.CharField(max_length=100)
    recognized_info = models.CharField(max_length=100)
    accuracy = models.CharField(max_length=100)
    date = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    violation_type = models.CharField(max_length=100)

    def __str__(self):
        return f"ALPR Recognition ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_alpr_recognition_result'


class ALPRRecognizedImageDatabaseTrafficLight(models.Model):
    """
    This model is used to store the information of the recognized image by the OCR.
    """
    recognized_image_path = models.CharField(max_length=500)

    def __str__(self):
        return f"ALPR Recognition ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_alpr_recognized_images_path_information'


class ALPRNonRecognizedImageDatabaseTrafficLight(models.Model):
    """
    This model is used to store the information of the non-recognized image by the OCR.
    """
    non_recognized_image_path = models.CharField(max_length=500)

    def __str__(self):
        return f"ALPR Recognition ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_alpr_non_recognized_images_path_information'


class DeletedImage(models.Model):
    """
    This model is used to store the deleted images.
    """
    original_image_id = models.IntegerField()
    original_image_path = models.CharField(max_length=500)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DeletedImage ID: {self.id}"

    class Meta:
        db_table = 'traffic_light_deleted_images'
