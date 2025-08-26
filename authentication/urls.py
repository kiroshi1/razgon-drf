from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .html_views import dashboard_view, login_view, logout_view, profile_view, register_view
from .views import AuthViewSet

# API Routes
router = DefaultRouter()
router.register(r"api", AuthViewSet, basename="auth")

urlpatterns = [
    # API endpoints
    path("", include(router.urls)),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
