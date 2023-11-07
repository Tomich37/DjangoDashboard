from django.urls import path
from authentication import views as auth

urlpatterns = [
    path('login/', auth.login, name='login'),
]
