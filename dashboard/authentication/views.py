from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseServerError
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout

from logs.SetLogs import SetLogs
from authentication.models import UsersModel

logger = SetLogs().logger

def main():
    return HttpResponsePermanentRedirect("/login")

def login(request):
    try:
        return render(request, 'login.html')
    except Exception as e:
        print(f'ошибка в login: {e}')
        logger.exception(f'ошибка в login: {e}')

def logout_view(request):
    logout(request)
    # Пользователь успешно вышел, перенаправьте его на нужную страницу
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Пользователь успешно вошел, перенаправьте его на нужную страницу
            return redirect('dashboard')
        else:
            # Ошибка аутентификации, покажите сообщение об ошибке
            messages.error(request, 'Неправильный логин или пароль.')
    return render(request, 'login.html')