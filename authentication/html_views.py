from django.shortcuts import render


def login_view(request):
    """Страница входа в систему (API-версия)"""
    if request.method == "GET":
        return render(request, "auth/api_login.html")


def register_view(request):
    """Страница регистрации (API-версия)"""
    if request.method == "GET":
        return render(request, "auth/api_register.html")


def dashboard_view(request):
    """Личный кабинет пользователя (API-версия)"""
    return render(request, "dashboard/api_dashboard.html")


# Профиль и выход теперь работают через API в JavaScript
