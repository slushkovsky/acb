from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

import server.views as server


partner_urls = [
    url(r'^login',          server.partner.login_view,           name='login'),
    url(r'^logout/$',       server.partner.logout_view,          name='logout'),
    url(r'^registration/$', server.partner.registration_view,    name='registration'),
    url(r'^settings/$',     server.partner.settings_view,        name='settings'),
    url(r'^dashboard/$',    server.partner.dashboard_view,       name='dashboard'),
    url(r'^instructors/$',  server.partner.instructors_list_view),
]

api_urls = [
    url(r'^api/employees/$', server.rest.InstructorView.as_view()),
    url(r'^api/cars/$',      server.rest.CarView       .as_view()),
    url(r'^api/waybills/$',  server.rest.WaybillView   .as_view())
]

static_urls = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = static_urls + api_urls + partner_urls + [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
] 