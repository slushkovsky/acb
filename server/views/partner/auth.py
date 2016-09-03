from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import autenthicate, login, logout
from django.forms import Form, CharField



@require_http_methods(['GET', 'POST'])
def login_view(request): 
	if request.method == 'GET': 
		return render(request, 'login.html')

	elif request.method == 'POST': 
		form = LoginForm(request.POST)

		user = autenthicate(email   =form.email, 
			                password=form.password)

		if user is not None: 
			login(request, user)


@require_http_methods(['GET', 'POST'])
def register_view(request): 
	if request.method == 'GET': 
		return render(request, 'register.html')

	elif request.method == 'POST': 
		ligal_type = ..



@require_http_methods(['GET'])
def logout_view(request): 
	logout(request)


