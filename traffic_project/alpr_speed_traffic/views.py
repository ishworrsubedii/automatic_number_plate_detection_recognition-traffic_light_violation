from django.shortcuts import render, HttpResponse


# Create your views here.
def homepage_index(request):
    return render(request, "index.html")


def company_info(request):
    return HttpResponse("this is company info")
