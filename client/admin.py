from django.contrib import admin
from .models import *


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')


@admin.register(BidState)
class BidStateAdmin(admin.ModelAdmin):
    list_display = ('BidID', 'state')
