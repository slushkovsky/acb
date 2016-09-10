from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from server.models import Instructor


@require_http_methods(['GET', 'POST', 'PATCH', 'DELETE'])
@login_required
def instructor_view(request, id=None): 
	if request.method == 'GET': 
		return render(request, 'instructor.html', {
			'instructor': get_object_or_404(Instructor, id),
			'mode': 'edit'
		})

	elif request.method == 'POST': 
		pass # Add new instructor

	elif request.method == 'PATCH': 
		pass # Patch instructor (with id) params 

	elif request.method == 'DELETE': 
		pass # Delete instructor with id
	