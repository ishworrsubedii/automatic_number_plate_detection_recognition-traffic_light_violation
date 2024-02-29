import os
import shutil

from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .trafficlightservices import TrafficLightViolationService
from .serializers import (
    ImageCaptureSerializer,
    TrafficlightColorDetectionSerializer,
    VehicleDetectionSerializer,
    NumberPlateDetectionSerializer,
    NumberPlateRecognitionSerializer,
    RedLightViolatedVehiclesListSerializer,
    VehicleNotDetectedImageListSerializer,
    ALPRRecognitionResultSerializer,
    ALPRRecognizedImageSerializer,
    ALPRNonRecognizedImageSerializer,
)
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
    DeletedImage
)


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


traffic_light_services = TrafficLightViolationService()


class ImageCaptureStartView(APIView):
    """
    View to start image capture
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        traffic_light_services.start_image_capture_traffic_light()
        return Response({"message": "Image capture started"}, status=status.HTTP_200_OK)


class ImageCaptureStopView(APIView):
    """
    View to stop image capture
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        traffic_light_services.stop_image_capture_traffic_light()
        return Response({"message": "Image capture stopped"}, status=status.HTTP_200_OK)


class TrafficLightColorDetectionStartView(APIView):
    """
    View to start traffic light color detection
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        traffic_light_services.start_traffic_light_color_detection()
        return Response({"message": "Traffic light color detection started"}, status=status.HTTP_200_OK)


class TrafficLightColorDetectionStopView(APIView):
    """
        View to stop traffic light color detection
        """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        traffic_light_services.stop_traffic_light_color_detection()
        return Response({"message": "Traffic light color detection stopped"}, status=status.HTTP_200_OK)


class VehicleDetectionPolygonStartView(APIView):
    """
    View to start vehicle detection polygon
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        traffic_light_services.start_vehicle_detection_polygon()
        return Response({"message": "Vehicle detection polygon started"}, status=status.HTTP_200_OK)


class VehicleDetectionPolygonStopView(APIView):
    """
    View to stop vehicle detection polygon
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        traffic_light_services.stop_vehicle_detection_polygon()
        return Response({"message": "Vehicle detection polygon stopped"}, status=status.HTTP_200_OK)


class NumberPlateDetectionStartView(APIView):
    """
    View to start number plate detection
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        traffic_light_services.start_number_plate_detection()
        return Response({"message": "Number plate detection started"}, status=status.HTTP_200_OK)


class NumberPlateDetectionStopView(APIView):
    """
    View to stop number plate detection
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        traffic_light_services.stop_number_plate_detection()
        return Response({"message": "Number plate detection stopped"}, status=status.HTTP_200_OK)


class AutomaticNumberPlateRecogniztionStartView(APIView):
    """
    View to start automatic number plate recognition
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        traffic_light_services.start_automatic_number_plate_recognition()
        return Response({"message": "Automatic number plate recognition started"}, status=status.HTTP_200_OK)


class AutomaticNumberPlateRecogniztionStopView(APIView):
    """
    View to stop automatic number plate recognition
    """
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        traffic_light_services.stop_automatic_number_plate_recognition()
        return Response({"message": "Automatic number plate recognition stopped"}, status=status.HTTP_200_OK)


# Get Request
class CaptureStatusView(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        captures = ImageCaptureDatabaseTrafficLight.objects.all()
        serializer = ImageCaptureSerializer(captures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ColorDetectionStatusView(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        detections = TrafficlightColorDetectionTrafficlight.objects.all()
        serializer = TrafficlightColorDetectionSerializer(detections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VehicleDetectionStatusView(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        detections = VehicleDetectionTrafficLight.objects.all()
        serializer = VehicleDetectionSerializer(detections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NumberPlateDetectionStatusView(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        detections = NumberPlateDetectionTrafficLight.objects.all()
        serializer = NumberPlateDetectionSerializer(detections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NumberPlateRecognitionStatusView(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        recognitions = NumberPlateRecognitionTrafficLight.objects.all()
        serializer = NumberPlateRecognitionSerializer(recognitions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RedLightViolatedVehiclesListView(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        violations = RedLightViolatedVehiclesListTrafficLight.objects.all()
        serializer = RedLightViolatedVehiclesListSerializer(violations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VehicleNotDetectedImageView(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        images = VehicleNotDetectedImageListDatabaseTrafficLight.objects.all()
        serializer = VehicleNotDetectedImageListSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ALPRRecognitionResultView(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        results = ALPRRecognitionResultDatabaseTrafficLight.objects.all()
        serializer = ALPRRecognitionResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ALPRRecognizedImageView(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        images = ALPRRecognizedImageDatabaseTrafficLight.objects.all()
        serializer = ALPRRecognizedImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ALPRNonRecognizedImageView(APIView):
    authentication_classes = [JWTAuthentication, CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(self, request):
        images = ALPRNonRecognizedImageDatabaseTrafficLight.objects.all()
        serializer = ALPRNonRecognizedImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
