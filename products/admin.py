from django.contrib import admin
from .models import Candle, RoomSpray
# Register your models here.

@admin.register(Candle)
class CandleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(RoomSpray)
class RoomSprayAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')