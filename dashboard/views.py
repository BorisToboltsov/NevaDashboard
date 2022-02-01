from django.shortcuts import render

# Create your views here.
from dashboard.forms import DashboardDate
import datetime

from dashboard.models import Group


def check_in(request):
    if request.method == 'POST':
        form = DashboardDate(data=request.POST)
        start_date = datetime.datetime.strptime(request.POST.get('start_date'), '%d-%m-%Y').date()
        end_date = datetime.datetime.strptime(request.POST.get('end_date'), '%d-%m-%Y').date()
        data_range = end_date - start_date
        dates = list()
        for days in range(0, data_range.days + 1):
            dates.append((start_date + datetime.timedelta(days)).isoformat())
        start_date_30 = start_date - datetime.timedelta(30)
        end_date_30 = end_date + datetime.timedelta(30)
        # groups = Group.objects.values()  # Выбор всех групп
        groups = Group.objects.filter(arrival_date__gte=start_date_30).filter(departure_date__lte=end_date_30).values()
        for i in groups:
            i['arrival_date'] = i['arrival_date'].date().isoformat()
            i['departure_date'] = i['departure_date'].date().isoformat()

    else:
        form = DashboardDate()
        dates = list()
        groups = []
    context = {
        'title': 'Dashboard график заездов',
        'url': 'dashboard:check_in',
        'form': form,
        'dates': dates,
        'groups': groups,
    }
    return render(request, 'dashboard/check_in.html', context)


def hotels(request):
    context = {
        'title': 'Dashboard отели',
    }
    return render(request, 'dashboard/hotels.html', context)


def transports(request):
    if request.method == 'POST':
        form = DashboardDate(data=request.POST)
        start_date = datetime.datetime.strptime(request.POST.get('start_date'), '%d-%m-%Y').date()
        end_date = datetime.datetime.strptime(request.POST.get('end_date'), '%d-%m-%Y').date()
        data_range = end_date - start_date
        dates = list()
        for days in range(0, data_range.days+1):
            dates.append((start_date + datetime.timedelta(days)).isoformat())
        groups = Group.objects.values()  # Выбор всех групп
        # groups = Group.objects.filter(arrival_date__gte=start_date).filter(departure_date__lte=end_date).values()
        for i in groups:
            i['arrival_date'] = i['arrival_date'].date().isoformat()
            i['departure_date'] = i['departure_date'].date().isoformat()

    else:
        form = DashboardDate()
        dates = list()
        groups = []
    context = {
        'title': 'Dashboard транспорт',
        'url':  'dashboard:transports',
        'form': form,
        'dates': dates,
        'groups': groups,
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
