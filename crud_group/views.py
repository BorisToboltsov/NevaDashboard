from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from crud_group.forms import AddGroupForm
from dashboard.models import Group

# Create your views here.
from django.views.generic import CreateView


# class AddGroup(CreateView):
#     template_name = 'addgroup.html'


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def add_group(request):
    context = {
        'forms': AddGroupForm,
    }
    return render(request, 'crud_group/addgroup.html', context)


def detail_group(request, pk):
    group = Group.objects.get(pk=pk)
    context = {
        'group': group
    }
    return render(request, 'crud_group/detailgroup.html', context)
