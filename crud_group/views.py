from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


# class AddGroup(CreateView):
#     template_name = 'addgroup.html'


def add_group(request):
    return render(request, 'crud_group/addgroup.html')
