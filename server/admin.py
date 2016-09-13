from django.contrib import admin
from .models import Car, Instructor, Waybill, City, District, Bid

admin.site.site_header = 'ACB Admin'
admin.site.site_title  = 'ACB'

admin.site.register(Car)
admin.site.register(District)
admin.site.register(City)
admin.site.register(Waybill)
admin.site.register(Instructor)
admin.site.register(Bid)