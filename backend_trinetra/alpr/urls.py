from django.urls import path
from .views import (
    ImageCaptureStartView,
    ImageCaptureStopView,
    ImageLoadStartView,
    ImageLoadStopView,
    ALPRStartView,
    ALPRStopView, ImageCaptureStatus, ImageLoadStatus, ALPRStatus, ALPRecognitionList, ALPRcognizedImageList,
    ALPNonRcognizedImageList,
)

urlpatterns = [
    # start and stop paths
    path('image_capture/start/', ImageCaptureStartView.as_view(), name='image_capture_start'),
    path('image_capture/stop/', ImageCaptureStopView.as_view(), name='image_capture_stop'),
    path('image_load/start/', ImageLoadStartView.as_view(), name='image_load_start'),
    path('image_load/stop/', ImageLoadStopView.as_view(), name='image_load_stop'),
    path('alpr/start/', ALPRStartView.as_view(), name='alpr_start'),
    path('alpr/stop/', ALPRStopView.as_view(), name='alpr_stop'),
    # status paths
    path('image_capture_status/', ImageCaptureStatus.as_view(), name='image_capture_status'),
    path('image_load_status/', ImageLoadStatus.as_view(), name='image_load_status'),
    path('alpr_status/', ALPRStatus.as_view(), name='alpr_status'),
    path('alpr_recognition_data/', ALPRecognitionList.as_view(), name='alp_recognition_list'),

    # image paths
    path('alpr_recognized_image_paths/', ALPRcognizedImageList.as_view(), name='alpr_recognized_image_paths'),
    path('alpr_non_recognized_image_paths/', ALPNonRcognizedImageList.as_view(), name='alpr_recognized_image_paths'),

]
