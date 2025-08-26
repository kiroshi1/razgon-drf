from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("health/", views.health_check, name="health_check"),
]
