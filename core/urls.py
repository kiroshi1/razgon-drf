from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

from authentication.html_views import (
    dashboard_view,
    login_view,
    logout_view,
    profile_view,
    register_view,
)


# Redirect root to dashboard
def root_redirect(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("login")


urlpatterns = [
    path("", root_redirect, name="root"),
    path("admin/", admin.site.urls),
    # HTML Views
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("profile/", profile_view, name="profile"),
    path("logout/", logout_view, name="logout"),
    # API endpoints
    path("api/auth/", include("authentication.urls")),
    path("api/drf-auth/", include("rest_framework.urls")),  # DRF browsable API auth
    path("api/cars/", include("cars.urls")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
