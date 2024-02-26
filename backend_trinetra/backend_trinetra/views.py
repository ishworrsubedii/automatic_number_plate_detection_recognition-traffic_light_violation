from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
import os


def index(request, *args, **kwargs):
    return render(request, 'index.html')


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


@login_required
def protected_serve(request, path):
    file_path = os.path.join(settings.STATIC_ROOT, path)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'))
    else:
        raise Http404
