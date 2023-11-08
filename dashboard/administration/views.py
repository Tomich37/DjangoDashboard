from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

from logs.SetLogs import SetLogs
from authentication.models import UsersModel

logger = SetLogs().logger

@login_required
def admin_page(request):
    user = request.user
    if user.is_superuser:
        return render(request, 'admin_page.html')
    else:
        logout(request)
        return redirect('login')

@login_required
@csrf_exempt    
def create_user(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        if not login or not password:
            return JsonResponse({'success': False, 'message': 'Login and password are required.'})

        if UsersModel.objects.filter(login=login).exists():
            return JsonResponse({'success': False, 'message': 'A user with this login already exists.'})
    
        hashed_password = make_password(password)
        user = UsersModel(login=login, password=hashed_password)
        user.save()
        return JsonResponse({'success': True, 'message': 'The user has been successfully created.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
