from django.contrib import admin
from .models import (ImageCaptureDatabaseTrafficLight,
                     TrafficlightColorDetectionTrafficlight,
                     VehicleDetectionTrafficLight,
                     NumberPlateDetectionTrafficLight,
                     NumberPlateRecognitionTrafficLight,
                     RedLightViolatedVehiclesListTrafficLight,
                     VehicleNotDetectedImageListDatabaseTrafficLight,
                     ALPRRecognitionResultDatabaseTrafficLight,
                     ALPRRecognizedImageDatabaseTrafficLight,
                     ALPRNonRecognizedImageDatabaseTrafficLight,
                     DeletedImage)

admin.site.register(ImageCaptureDatabaseTrafficLight)
admin.site.register(TrafficlightColorDetectionTrafficlight)
admin.site.register(VehicleDetectionTrafficLight)
admin.site.register(NumberPlateDetectionTrafficLight)
admin.site.register(NumberPlateRecognitionTrafficLight)
admin.site.register(RedLightViolatedVehiclesListTrafficLight)
admin.site.register(VehicleNotDetectedImageListDatabaseTrafficLight)
admin.site.register(ALPRRecognitionResultDatabaseTrafficLight)
admin.site.register(ALPRRecognizedImageDatabaseTrafficLight)
admin.site.register(ALPRNonRecognizedImageDatabaseTrafficLight)
admin.site.register(DeletedImage)
