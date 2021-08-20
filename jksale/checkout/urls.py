from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkoutView, name="checkout-view"),
    path('tracking/', views.trackingView, name="tracking-view"),
    path('order-confirmation/', views.orderConfirmationView, name="order-confirmation-view"),
    
]
