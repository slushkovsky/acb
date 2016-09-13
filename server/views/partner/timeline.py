from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from server.models import Event


@require_http_methods(['GET', 'POST', 'PATCH', 'DELETE'])
@login_required
def timeline_view(request, instructor_id=None):
    if request.method == 'GET': 
        return render(request, 'timeline/timeline.html', {
            'events': Event.objects.filter(partisipants__id__contains=instructor_id)
        })

    elif request.method == 'POST': 
        pass # Add new event

    elif request.method == 'PATCH':
        pass # Patch event 

    elif request.method == 'DELETE': 
        pass # Delete event