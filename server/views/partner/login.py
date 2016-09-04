from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.forms import Form, CharField, EmailField
from django.contrib import messages

from server.utils import flash_form_errors


class LoginForm(Form):
    email = EmailField() 
    password = CharField()


@require_http_methods(['GET', 'POST'])
def login_view(request): 
    if request.method == 'POST': 
        form = LoginForm(request.POST)

        if form.is_valid(): 
            user = authenticate(email   =form.cleaned_data['email'], 
                                password=form.cleaned_data['password'])

            if user is not None: 
                login(request, user)
                return HttpResponse('OK')
            else: 
            	messages.error(request, 'Unknown user with such email/password')
        else: 
            flash_form_errors(request, form)

    return render(request, 'login/login.html')