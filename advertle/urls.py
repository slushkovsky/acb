from django.conf.urls import url, include
from django.contrib import admin

from car_ways import views

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'employees/', views.InstructorView.as_view()),
    url(r'cars/',      views.CarView       .as_view()),
    url(r'waybills/',  views.WaybillView   .as_view()),

    url(r'add_instructor', views.add_instructor),
    url(r'timeline',       views.timeline),

    url(r'^admin/', admin.site.urls),
]
