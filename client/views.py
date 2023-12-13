from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import *
from datetime import datetime
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Аутентификация прошла успешна!')
                else:
                    return HttpResponse('Аккаунт неактивен!')
            else:
                return HttpResponse('Аккаунт не существует')
    else:
        form = LoginForm()
    return render(request,
                  'account/login.html,',
                  {'form': form})

def index(request):
    return render(request, 'client/index.html')


def baza_auth(request):
    return render(request, 'Admin/baza-auth.html')


def postclient(request):
    if request.method == 'POST':
        bid = Bid()
        bid.number = request.POST.get("number")
        bid.name = request.POST.get("name")
        bid.descr = request.POST.get("descr")
        bid.date = datetime.now().date()
        bid.save()
    return render(request, 'client/success.html')


class ClientView(View):
    def get(self, request):
        clients = Bid.objects.all()
        return render(request, 'Admin/baza.html', {'client_list': clients})





