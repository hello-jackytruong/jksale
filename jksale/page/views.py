from django.shortcuts import render

# Create your views here.
def homeView(request):
    context = {

    }
    return render(request, 'home.html', context)

def contactView(request):
    context = {

    }
    return render(request, 'contact.html', context)
