from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('dashboard:check_in'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form_profile = UserProfileForm(request.POST)
        if form.is_valid():
            form = form.save()
            form_profile = form_profile.save(commit=False)
            form_profile.user_id = form
            form_profile.save()
            return HttpResponseRedirect(reverse('dashboard:check_in'))
    else:
        form = UserRegisterForm()
        form_profile = UserProfileForm()
    context = {
        'title': 'Регистрация',
        'form': form,
        'form_profile': form_profile,
    }
    return render(request, 'authapp/register.html', context)


@login_required
def profile(request):
    context = {
        'title': 'Профайл'
    }
    return render(request, 'authapp/profile.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('authapp:login'))
