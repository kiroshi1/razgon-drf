from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .serializers import UserProfileSerializer, UserRegistrationSerializer


def login_view(request):
    """Страница входа в систему"""
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "GET":
        return render(request, "auth/login.html")

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            error_html = """
            <div class="rounded-md bg-red-50 border border-red-200 p-4 mb-4">
                <div class="text-sm text-red-700">
                    Необходимо указать имя пользователя и пароль.
                </div>
            </div>
            """
            return HttpResponse(error_html)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                # Если это HTMX запрос, перенаправляем на dashboard
                if request.htmx:
                    response = HttpResponse()
                    response["HX-Redirect"] = "/dashboard/"
                    return response
                return redirect("dashboard")
            else:
                error_html = """
                <div class="rounded-md bg-red-50 border border-red-200 p-4 mb-4">
                    <div class="text-sm text-red-700">
                        Аккаунт пользователя отключен.
                    </div>
                </div>
                """
                return HttpResponse(error_html)
        else:
            error_html = """
            <div class="rounded-md bg-red-50 border border-red-200 p-4 mb-4">
                <div class="text-sm text-red-700">
                    Неверные учетные данные.
                </div>
            </div>
            """
            return HttpResponse(error_html)


def register_view(request):
    """Страница регистрации"""
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "GET":
        return render(request, "auth/register.html")

    elif request.method == "POST":
        serializer = UserRegistrationSerializer(data=request.POST)

        if serializer.is_valid():
            user = serializer.save()
            auth_login(request, user)

            # Если это HTMX запрос, перенаправляем на dashboard
            if request.htmx:
                response = HttpResponse()
                response["HX-Redirect"] = "/dashboard/"
                return response
            return redirect("dashboard")
        else:
            # Формируем HTML с ошибками
            errors_html = '<div class="rounded-md bg-red-50 border border-red-200 p-4 mb-4"><div class="text-sm text-red-700">'

            for field, field_errors in serializer.errors.items():
                if field == "non_field_errors":
                    for error in field_errors:
                        errors_html += f"<p>{error}</p>"
                else:
                    field_name = {
                        "username": "Имя пользователя",
                        "email": "Email",
                        "password": "Пароль",
                        "password_confirm": "Подтверждение пароля",
                        "first_name": "Имя",
                        "last_name": "Фамилия",
                    }.get(field, field)

                    for error in field_errors:
                        errors_html += f"<p><strong>{field_name}:</strong> {error}</p>"

            errors_html += "</div></div>"
            return HttpResponse(errors_html)


@login_required
def dashboard_view(request):
    """Личный кабинет пользователя"""
    return render(request, "dashboard/dashboard.html")


@login_required
def profile_view(request):
    """Профиль пользователя"""
    if request.method == "GET":
        return render(request, "dashboard/profile_edit.html")

    elif request.method == "PATCH":
        serializer = UserProfileSerializer(request.user, data=request.POST, partial=True)

        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Профиль успешно обновлен!")

            # Возвращаем обновленное содержимое профиля
            return render(request, "dashboard/dashboard.html")
        else:
            # Формируем HTML с ошибками
            errors_html = '<div class="rounded-md bg-red-50 border border-red-200 p-4 mb-4"><div class="text-sm text-red-700">'

            for field, field_errors in serializer.errors.items():
                field_name = {"email": "Email", "first_name": "Имя", "last_name": "Фамилия"}.get(
                    field, field
                )

                for error in field_errors:
                    errors_html += f"<p><strong>{field_name}:</strong> {error}</p>"

            errors_html += "</div></div>"
            return HttpResponse(errors_html)


@require_http_methods(["POST"])
def logout_view(request):
    """Выход из системы"""
    auth_logout(request)

    if request.htmx:
        response = HttpResponse()
        response["HX-Redirect"] = "/login/"
        return response

    return redirect("login")
