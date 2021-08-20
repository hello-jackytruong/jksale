
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blogView, name="blog-view"),
    path('blog/<slug:slug>/', views.blogDetailView, name="blog-detail-view"),
    
]