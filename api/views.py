from django.shortcuts import render

from rest_framework.views import APIView


def api(request):
    return render(request)
