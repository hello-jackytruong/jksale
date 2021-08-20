from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shopView, name="shop-view"),
    path('product/', views.shopView, name="shop-view"),
    
    path('product/<slug:slug>/', views.productView, name="product-view"),
    
]
