from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from server.models import DrivingGround


@require_http_methods('GET')
@login_required
def places_list_view(request):
    return render(request, 'places_list/list.html', {
        'items': DrivingGround.objects.all()
    })
