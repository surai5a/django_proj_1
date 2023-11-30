from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('postclient/', postclient),
    path('baza/', ClientView.as_view()),
    path('baza-auth/', baza_auth)

]