from django.shortcuts import render

# Create your views here.
from dashboard.forms import DashboardDate
import datetime

from dashboard.models import Group


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
    if request.method == 'POST':
        form = DashboardDate(data=request.POST)
        start_date = datetime.datetime.strptime(request.POST.get('start_date'), '%d-%m-%Y')
        end_date = datetime.datetime.strptime(request.POST.get('end_date'), '%d-%m-%Y')
        data_range = end_date - start_date
        dates = list()
        dates.append(start_date.strftime('%d.%m.%y'))
        for days in range(1, data_range.days+1):
            dates.append((start_date + datetime.timedelta(days)).strftime('%d.%m.%y'))

        groups = Group.objects.values()
        for i in groups:
            i['arrival_date'] = i['arrival_date'].strftime('%d.%m.%y')
            i['departure_date'] = i['departure_date'].strftime('%d.%m.%y')

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
