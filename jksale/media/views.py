from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ImageMedia

# Create your views here.
def ImageMediaView(request):
    image_media = ImageMedia.objects.all()
    context = {
        'image_media':image_media,
    }
    return render(request, 'image-media.html', context)

    
