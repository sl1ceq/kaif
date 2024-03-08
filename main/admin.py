from django.contrib import admin
from .models import Order


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['instagram_nickname', 'pause', 'place', 'ordered']
    list_filter = ['ordered']