from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import *
from datetime import datetime
from django.views.generic.base import View


def index(request):
    return render(request, 'client/index.html')


def baza_auth(request):
    return render(request, 'client/baza-auth.html')


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
        return render(request, 'client/baza.html', {'client_list': clients})





