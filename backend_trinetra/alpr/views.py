from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .alprservices import ALPRServices
from .models import ImageCaptureDatabase, ImageLoadDatabase, ALPRDatabase, ALPRecognitionDatabase, \
    ALPRRecognizedImageDatabase, ALPRNonRecognizedImageDatabase
from .serializers import ALPRecognitionSerializer, AlPRecogniizedImagePathsSerializer, \
    AlPNonRecogniizedImagePathsSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


alpr_services = ALPRServices()


class ImageCaptureStartView(APIView):
    """
    View to start image capture
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        alpr_services.start_image_capture()
        return Response({"message": "Image capture started"}, status=status.HTTP_200_OK)


class ImageCaptureStopView(APIView):
    """
    View to stop image capture
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        alpr_services.stop_image_capture()
        return Response({"message": "Image capture stopped"}, status=status.HTTP_200_OK)


class ImageLoadStartView(APIView):
    """
    View to start image load
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        alpr_services.start_load_image()
        return Response({"message": "Image load started"}, status=status.HTTP_200_OK)


class ImageLoadStopView(APIView):
    """
    View to stop image load
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        alpr_services.stop_load_image()
        return Response({"message": "Image load stopped"}, status=status.HTTP_200_OK)


class ALPRStartView(APIView):
    """
    View to start ALPR (Automatic License Plate Recognition)
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        alpr_services.start_recognize_plate()
        return Response({"message": "ALPR started"}, status=status.HTTP_200_OK)


class ALPRStopView(APIView):
    """
    View to stop ALPR (Automatic License Plate Recognition)
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        alpr_services.stop_recognize_plate()
        return Response({"message": "ALPR stopped"}, status=status.HTTP_200_OK)


class ImageCaptureStatus(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        try:
            latest_capture = ImageCaptureDatabase.objects.latest('id')
            data = {
                'start_time': latest_capture.started_at,
                'status': latest_capture.status
            }
            return Response(data, status=status.HTTP_200_OK)
        except ImageCaptureDatabase.DoesNotExist:
            return Response({'error': 'No capture data available'}, status=status.HTTP_404_NOT_FOUND)


class ImageLoadStatus(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        try:
            latest_load = ImageLoadDatabase.objects.latest('id')
            data = {
                'start_time': latest_load.started_at,
                'status': latest_load.status
            }
            return Response(data, status=status.HTTP_200_OK)
        except ImageLoadDatabase.DoesNotExist:
            return Response({'error': 'No load data available'}, status=status.HTTP_404_NOT_FOUND)


class ALPRStatus(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        try:
            latest_alpr = ALPRDatabase.objects.latest('id')
            data = {
                'start_time': latest_alpr.started_at,
                'status': latest_alpr.status
            }
            return Response(data, status=status.HTTP_200_OK)
        except ALPRDatabase.DoesNotExist:
            return Response({'error': 'No ALPR data available'}, status=status.HTTP_404_NOT_FOUND)


class ALPRecognitionList(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        recognitions = ALPRecognitionDatabase.objects.all()
        serializer = ALPRecognitionSerializer(recognitions, many=True)
        return Response(serializer.data)


# To store the information or image path of recognized image and non recognized model by the ocr

class ALPRcognizedImageList(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        recognized_images = ALPRRecognizedImageDatabase.objects.all()
        serializer = AlPRecogniizedImagePathsSerializer(recognized_images, many=True)
        return Response(serializer.data)


class ALPNonRcognizedImageList(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        recognized_images = ALPRNonRecognizedImageDatabase.objects.all()
        serializer = AlPNonRecogniizedImagePathsSerializer(recognized_images, many=True)
        return Response(serializer.data)
