from django.contrib import admin
from .models import Candle, RoomSpray

# Register your models here.

@admin.register(Candle)
class CandleAdmin(admin.ModelAdmin):
    """
    Admin view configuration for Candle model.
    """
    list_display = ('name', 'price')


@admin.register(RoomSpray)
class RoomSprayAdmin(admin.ModelAdmin):
    """
    Admin view configuration for RoomSpray model.
    """
    list_display = ('name', 'price')
