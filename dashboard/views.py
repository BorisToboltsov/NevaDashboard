from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from dashboard.forms import DashboardDate
import datetime

from dashboard.models import Group


@login_required
def check_in(request):
    if request.method == 'POST':
        form = DashboardDate(data=request.POST)
        start_date = datetime.datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
        data_range = end_date - start_date
        dates = list()
        for days in range(0, data_range.days + 1):
            dates.append((start_date + datetime.timedelta(days)).isoformat())
        start_date_30 = start_date - datetime.timedelta(30)
        end_date_30 = end_date + datetime.timedelta(30)
        # groups = Group.objects.values()  # Выбор всех групп
        groups = Group.objects.filter(arrival_date_group__gte=start_date_30).filter(departure_date_group__lte=end_date_30).values()
        for i in groups:
            i['arrival_date_group'] = i['arrival_date_group'].isoformat()
            i['departure_date_group'] = i['departure_date_group'].isoformat()

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


@login_required
def hotels(request):
    context = {
        'title': 'Dashboard отели',
    }
    return render(request, 'dashboard/hotels.html', context)


@login_required
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
            print(i['arrival_date'])
            i['arrival_date_group'] = i['arrival_date_group'].date().isoformat()
            i['departure_date_group'] = i['departure_date_group'].date().isoformat()

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


@login_required
def museums(request):
    context = {
        'title': 'Dashboard музеи',
        'hotel': 'Гостиница Москва'
    }
    return render(request, 'dashboard/museums.html', context)


@login_required
def food(request):
    context = {
        'title': 'Dashboard питание',
    }
    return render(request, 'dashboard/food.html', context)
