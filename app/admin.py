from django.contrib import admin

from app.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model')
    