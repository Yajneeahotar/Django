# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    

    path('login/', views.login_view, name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('customlogin/', views.login_view, name='loginview'),

    path('logout_custom/', views.logout_view, name='logout_custom'),
]

'''path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'
    ), name='login'),'''