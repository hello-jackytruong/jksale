from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home-view"),
    path('contact/', views.contactView, name="contact-view"),
    
]
