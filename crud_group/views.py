from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from authapp.models import Employee
from crud_group.forms import AddGroupForm, AddGroupHotelForm
from dashboard.models import Group


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required
def add_group(request):
    if request.method == "POST":
        group = AddGroupForm(request.POST)
        hotel = AddGroupHotelForm(request.POST)
        group_form = group.save(commit=False)
        group_form.manager_id = Employee.objects.filter(user_id_id=request.user.id)[0]
        group_form = group_form.save()
        hotel_form = hotel.save(commit=False)
        hotel_form.group_id = group_form
        hotel_form.save()

    else:
        group_form = AddGroupForm()
        hotel = AddGroupHotelForm()
    context = {
        'group': group_form,
        'hotel': hotel,
    }
    return render(request, 'crud_group/addgroup.html', context)


@login_required
def detail_group(request, pk):
    group = Group.objects.get(pk=pk)
    context = {
        'group': group
    }
    return render(request, 'crud_group/detailgroup.html', context)
