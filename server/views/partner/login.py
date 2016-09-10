from logbook import Logger

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.forms import Form, CharField, EmailField
from django.contrib import messages

from server.utils import flash_form_errors

logger = Logger('AUTH')


class LoginForm(Form):
    email = EmailField() 
    password = CharField()


@require_http_methods(['GET', 'POST'])
def login_view(request): 
    if request.method == 'POST': 
        if request.user.is_authenticated():
            logger.warning('Authenticated user try to make POST request on /login')
            return HttpResponseBadRequest('You are always authenticated')

        form = LoginForm(request.POST)

        if form.is_valid(): 
            user = authenticate(email   =form.cleaned_data['email'], 
                                password=form.cleaned_data['password'])

            logger.debug('Login: {!r} try'.format(user.email))

            if user is not None: 
                login(request, user)

                logger.debug('Login: {!r} success'.format(user.email))

                if hasattr(request, 'next'): 
                    return redirect(request.next)
                else: 
                    return redirect('/dashboard')
            else: 
                logger.debug('Login: {!r} password fail'.format(user.email))
                messages.error(request, 'Unknown user with such email/password')
        else: 
            logger.debug('Login: Invalid form')

            flash_form_errors(request, form)

    if request.user.is_authenticated():
        return redirect('/dashboard')

    return render(request, 'login/login.html')


@require_http_methods(['GET'])
def logout_view(request): 
    logger.debug('Logout: {!r}'.format(request.user.email))
    logout(request)