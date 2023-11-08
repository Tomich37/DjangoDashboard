from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseServerError
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from logs.SetLogs import SetLogs
from authentication.models import UsersModel

logger = SetLogs().logger

@login_required
def dashboard(request):
    try:
        return HttpResponse('Test')
    except Exception as e:
        print(f'ошибка в login: {e}')
        logger.exception(f'ошибка в login/dashboard: {e}')
        return HttpResponseServerError()
