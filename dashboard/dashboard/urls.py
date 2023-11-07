from django.urls import path
from authentication import views as auth

urlpatterns = [
    path('login_view/', auth.login_view, name='login_view'),
    path("login/", auth.login, name='login'),
    path('', auth.main, name='main'),
]
