from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.loginView, name="login-view"),
    path('register/', views.registerView, name="register-view"),
    path('forgot-password/', views.forgotPasswordView, name="forgot-password-view"),
    path('logout/', views.logoutUser, name="logout-view"),
]
