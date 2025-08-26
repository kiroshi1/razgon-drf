from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import AuthViewSet

# API Routes
router = DefaultRouter()
router.register(r"api", AuthViewSet, basename="auth")

urlpatterns = [
    # API endpoints
    path("", include(router.urls)),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
