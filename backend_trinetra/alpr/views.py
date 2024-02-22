from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .alprservices import ALPRServices


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
