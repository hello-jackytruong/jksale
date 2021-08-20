from django.shortcuts import render, redirect
from .models import Posts
from django.http import HttpResponse

# Create your views here.

def blogView(request):
    post = Posts.objects.all()
    context = {
        'post':post,
    }
    return render(request, 'blog.html', context)

def blogDetailView(request, slug):
    post_details = Posts.objects.get(slug=slug)
    context = {
        'post_details':post_details,
    }
    return render(request, 'blog-detail.html', context)

