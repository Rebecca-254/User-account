from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('', views.home, name='home'),
    path('activate/<uid>/<token>/', views.activate, name='activate'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.profile_view, name='edit_profile'),  # alias for POST test
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]