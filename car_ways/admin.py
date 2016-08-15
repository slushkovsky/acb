from django.contrib import admin
from .models import Car, Instructor, Waybill, City, District

admin.site.site_header = 'ACB Admin'
admin.site.site_title = 'ACB'


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    pass


@admin.register(Waybill)
class WaybillAdmin(admin.ModelAdmin):
    pass
