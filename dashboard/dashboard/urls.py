from django.urls import path
from authentication import views as auth
from administration import views as admin
from board import views as board

urlpatterns = [
    path('login_view/', auth.login_view, name='login_view'),
    path("login/", auth.login, name='login'),
    path('logout/', auth.logout_view, name='logout'),
    path('', auth.main, name='main'),
    
    path("dashboard/", board.dashboard, name='dashboard'),
    
    path('admin_page/', admin.admin_page, name='admin_page'),
    path('create_user/', admin.create_user, name='create_user'),

]
