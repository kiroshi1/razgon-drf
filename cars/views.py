from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def health_check(request):
    """Проверка работы API"""
    return Response({"status": "ok", "message": "Cars API is running"})
