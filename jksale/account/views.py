from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth
from .models import User
from .models import Profile


# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account:login-view')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'login.html')

def registerView(request):
    context = {

    }
    return render(request, 'register.html', context)

def forgotPasswordView(request):
    context = {

    }
    return render(request, 'forgot-password.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('shop-view')
