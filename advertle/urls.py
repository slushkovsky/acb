from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

import server.views as server

urlpatterns = [
    url(r'^i18n/',          include('django.conf.urls.i18n')),
    url(r'^login/',         server.partner.login_view),
    url(r'^registration/',  server.partner.registration_view),
    url(r'^api/employees/', server.rest.InstructorView.as_view()),
    url(r'^api/cars/',      server.rest.CarView.as_view()),
    url(r'^api/waybills/',  server.rest.WaybillView.as_view()),
    url(r'^admin/',         admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
