from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import Employee
from crud_group.forms import AddGroupForm, AddGroupHotelForm
from dashboard.models import Group


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def add_group(request):
    if request.method == "POST":
        group = AddGroupForm(request.POST)
        hotel = AddGroupHotelForm(request.POST)
        # group.instance.manager_id_id = Employee.objects.get(user_id_id=request.user.id).user_id_id
        group_form = group.save()
        hotel_form = hotel.save(commit=False)
        hotel_form.group_id = group_form
        hotel_form.save()
        # employee = Employee.objects.filter(user_id_id=request.user.id)
        # print(request.user.id)
        # print(employee[0].first_name)
        # print(employee[0].user_id, 'user_id')
        # print(employee[0].user_id_id)

    else:
        group = AddGroupForm()
        hotel = AddGroupHotelForm()
        # employee = Employee.objects.filter(user_id_id=request.user.id)
    context = {
        'group': group,
        'hotel': hotel,
        # 'employee': employee,
    }
    return render(request, 'crud_group/addgroup.html', context)


def detail_group(request, pk):
    group = Group.objects.get(pk=pk)
    context = {
        'group': group
    }
    return render(request, 'crud_group/detailgroup.html', context)
