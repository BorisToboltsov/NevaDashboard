from django.shortcuts import render

# Create your views here.


def check_in(request):
    return render(request, 'dashboard/check_in.html')


def hotels(request):
    return render(request, 'dashboard/hotels.html')


def transports(request):
    return render(request, 'dashboard/transports.html')


def museums(request):
    return render(request, 'dashboard/museums.html')


def food(request):
    return render(request, 'dashboard/food.html')
