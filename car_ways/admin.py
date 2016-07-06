from django.contrib import admin
from .models import Car, Employe, Waybill


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    pass


@admin.register(Waybill)
class WaybillAdmin(admin.ModelAdmin):
    pass
