from django.shortcutrs import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


@require_http_methods(['GET', 'POST', 'PATCH', 'DELETE'])
@login_required
def timeline(request, id=None):
	if request.method == 'GET': 
		return render(request, 'timeline.html', {
			'events': Events.objects.filter()
		})

	elif request.method == 'POST': 
		pass # Add new event

	elif request.method == 'PATCH':
		pass # Patch event 

	elif request.method == 'DELETE': 
		pass # Delete event