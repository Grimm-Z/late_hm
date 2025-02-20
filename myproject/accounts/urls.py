from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('protected/', views.protected_view, name='protected'),
    path('', views.home, name='home'),
    ]