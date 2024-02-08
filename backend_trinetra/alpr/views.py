from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from services.alpr.usage.start.start_image_load import StartImageLoadExample
from services.alpr.usage.stop.stop_image_capture import StopImageCaptureExample
from services.alpr.usage.start.start_image_capture import StartImageCaptureExample
from services.alpr.usage.stop.stop_image_load import update_file

import time


class ImageCaptureView(APIView):
    """
    View to start and stop image capture
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        action = request.data.get('action')

        if action == 'start':
            flag_path = "services/alpr/resources/flag_check/capture_status.txt"
            source = 'rtsp://ishwor:subedi@192.168.1.106:5555/h264_opus.sdp'
            image_save_dir = "services/alpr/resources/rtsp"
            thres = 5

            image_capture_service = StartImageCaptureExample(flag_path, source, image_save_dir,
                                                             thres)
            image_capture_service.create_stop_flag()
            image_capture_service.start_service()
            time.sleep(1)

            return Response({"message": "Image capture started"}, status=status.HTTP_200_OK)

        elif action == 'stop':
            flag_path = "services/alpr/resources/flag_check/capture_status.txt"

            stop_service = StopImageCaptureExample(flag_path)
            stop_service.stop_image_capture_service()
            return Response({"message": "Image capture stopped"}, status=status.HTTP_200_OK)

        else:
            return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)


class ImageLoadView(APIView):
    """
    View to start and stop image load
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        action = request.data.get('action')

        if action == 'start':
            flag_path = "services/alpr/resources/flag_check/start_load_status.txt"
            image_dir = 'services/alpr/resources/rtsp/'
            model_path = 'services/alpr/resources/yolov8/nnpd.pt'
            image_save_dir = 'services/alpr/resources/plate_detected/'

            image_load_service = StartImageLoadExample(flag_path, image_dir, model_path, image_save_dir)
            image_load_service.create_stop_flag()
            image_load_service.start_service()

            time.sleep(1)

            return Response({"message": "Image load started"}, status=status.HTTP_200_OK)

        else:
            file_path = 'services/alpr/resources/flag_check/start_load_status.txt'
            update_file(file_path)
