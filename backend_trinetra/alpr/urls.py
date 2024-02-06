from django.urls import path
from .views import ImageCaptureView, ImageLoadView

urlpatterns = [
    path('image-capture/', ImageCaptureView.as_view(), name='image-capture'),
    path('image-load/', ImageLoadView.as_view(), name='image-load'),

]
