from django.shortcuts import render

# Create your views here.


def check_in(request):
    context = {
        'title': 'Dashboard график заездов',
    }
    return render(request, 'dashboard/check_in.html', context)


def hotels(request):
    context = {
        'title': 'Dashboard отели',
    }
    return render(request, 'dashboard/hotels.html', context)


def transports(request):
    context = {
        'title': 'Dashboard транспорт',
    }
    return render(request, 'dashboard/transports.html', context)


def museums(request):
    context = {
        'title': 'Dashboard музеи',
        'hotel': 'Гостиница Москва'
    }
    return render(request, 'dashboard/museums.html', context)


def food(request):
    context = {
        'title': 'Dashboard питание',
    }
    return render(request, 'dashboard/food.html', context)
