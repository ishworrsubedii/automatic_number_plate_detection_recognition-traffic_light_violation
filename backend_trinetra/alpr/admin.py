from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import ImageCaptureDatabase, ImageLoadDatabase, ALPRDatabase, ALPRecognitionDatabase, \
    ALPRRecognizedImageDatabase, ALPRNonRecognizedImageDatabase

admin.site.register(ImageCaptureDatabase)
admin.site.register(ImageLoadDatabase)
admin.site.register(ALPRDatabase)
admin.site.register(ALPRecognitionDatabase)
admin.site.register(ALPRRecognizedImageDatabase)
admin.site.register(ALPRNonRecognizedImageDatabase)
