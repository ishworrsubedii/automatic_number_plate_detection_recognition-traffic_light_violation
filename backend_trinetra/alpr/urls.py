from django.urls import path
from .views import (
    ImageCaptureStartView,
    ImageCaptureStopView,
    ImageLoadStartView,
    ImageLoadStopView,
    ALPRStartView,
    ALPRStopView,
)

urlpatterns = [
    path('image_capture/start/', ImageCaptureStartView.as_view(), name='image_capture_start'),
    path('image_capture/stop/', ImageCaptureStopView.as_view(), name='image_capture_stop'),
    path('image_load/start/', ImageLoadStartView.as_view(), name='image_load_start'),
    path('image_load/stop/', ImageLoadStopView.as_view(), name='image_load_stop'),
    path('alpr/start/', ALPRStartView.as_view(), name='alpr_start'),
    path('alpr/stop/', ALPRStopView.as_view(), name='alpr_stop'),
]
