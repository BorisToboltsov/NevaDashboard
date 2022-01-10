from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


def hotels(request):
    return render(request, 'dashboard/hotels.html')


def transports(request):
    return render(request, 'dashboard/transports.html')


def museums(request):
    return render(request, 'dashboard/museums.html')


def food(request):
    return render(request, 'dashboard/food.html')
