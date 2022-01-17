from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


def login(request):
    context = {
        'title': 'Авторизация'
    }
    return render(request, 'authapp/login.html', context)

def register(request):
    context = {
        'title': 'Регистрация'
    }
    return render(request, 'authapp/register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
