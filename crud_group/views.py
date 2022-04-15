from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from crud_group.forms import AddGroupForm, AddGroupHotelForm
from dashboard.models import Group

# Create your views here.
from django.views.generic import CreateView


# class AddGroup(CreateView):
#     template_name = 'addgroup.html'


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


# def add_group(request):
#     if request.method == "POST":
#         form = AddGroupForm(request.POST)
#         hotel = AddGroupHotelForm(request.POST)
#         form.save()
#         hotel.save()
#     else:
#         form = AddGroupForm()
#         hotel = AddGroupHotelForm()
#     context = {
#         'forms': form,
#         'hotel': hotel,
#     }
#     return render(request, 'crud_group/addgroup.html', context)

def add_group(request):
    if request.method == "POST":
        group = AddGroupForm(request.POST)
        hotel = AddGroupHotelForm(request.POST)
        group_form = group.save()
        hotel_form = hotel.save(commit=False)
        hotel_form.group_id = group_form
        hotel_form.save()
    else:
        group = AddGroupForm()
        hotel = AddGroupHotelForm()
    context = {
        'group': group,
        'hotel': hotel,
    }
    return render(request, 'crud_group/addgroup.html', context)


def detail_group(request, pk):
    group = Group.objects.get(pk=pk)
    context = {
        'group': group
    }
    return render(request, 'crud_group/detailgroup.html', context)
