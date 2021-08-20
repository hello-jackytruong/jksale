from django.shortcuts import render

# Create your views here.
def trackingView(request):
    context = {

    }
    return render(request, 'tracking-order.html', context)

def checkoutView(request):
    context = {

    }
    return render(request, 'checkout.html', context)

def orderConfirmationView(request):
    context = {

    }
    return render(request, 'confirmation.html', context)


