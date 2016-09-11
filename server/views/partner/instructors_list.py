from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from server.models import Instructor


@require_http_methods('GET')
@login_required
def instructors_list_view(request):
    return render(request, 'instructors_list/list.html', {
        'items': Instructor.objects.all()
    })
