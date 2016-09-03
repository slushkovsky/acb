from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.forms import Form, CharField, EmailField
from django.contrib import messages


class LoginForm(Form):
    email = EmailField() 
    password = CharField()


@require_http_methods(['GET', 'POST'])
def login_view(request): 
    if request.method == 'GET': 
        return render(request, 'login/login.html')

    elif request.method == 'POST': 
        form = LoginForm(request.POST)

        was_problems = False

        if form.is_valid(): 
            user = authenticate(email   =form.fields['email'], 
                                password=form.fields['password'])

            if user is not None: 
                login(request, user)
            else: 
            	was_problems = True
            	messages.error(request, 'Unknown user with such email/password')
        else: 
            for field, problems in form.errors.as_data().items():
                problems_msg = '<br>'.join(['- {}'.format(p.message) for p in problems])
                messages.error(request, '<b>Ivalid field {}:</b><br>{}'.format(field, problems_msg))

            was_problems = True

        if was_problems: 
            return render(request, 'login/login.html')

        return HttpResponse('OK')