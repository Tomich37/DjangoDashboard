from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseServerError
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from logs.SetLogs import SetLogs

logger = SetLogs().logger

@login_required
def dashboard(request):
    try:
        return render(request, 'dashboard.html')
    except Exception as e:
        print(f'ошибка в board/dashboard: {e}')
        logger.exception(f'ошибка в board/dashboard: {e}')
        return HttpResponseServerError()
