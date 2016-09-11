from logbook import Logger

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.forms import Form, EmailField, CharField
from django.contrib import messages
from emailusernames.utils import create_user

from server.models import Partner
from django.contrib.auth.models import User
from server.utils import flash_form_errors


logger = Logger('REGISTER')

class RegistrationFrom(Form): 
    legal_name = CharField() 
    address    = CharField()
    phone      = CharField(required=False)
    email      = EmailField()
    password   = CharField()


@require_http_methods(['GET', 'POST'])
def registration_view(request): 
    if request.method == 'POST':
        if request.user.is_authenticated(): 
            logger.warning('Authenticated user try to make POST request on /registration')
            return HttpResponseBadRequest('You are always authenticated')

        form = RegistrationFrom(request.POST)

        if form.is_valid(): 
            email      = form.cleaned_data['email']
            password   = form.cleaned_data['password']
            phone      = form.cleaned_data['phone']
            address    = form.cleaned_data['address']
            legal_name = form.cleaned_data['legal_name']

            try: 
                user = create_user(email=email, password=password)
                logger.debug('Created user with email {!r}'.format(email))

            except AttributeError as e: 
                logger.debug('Couldn\'t create user with email {!r} (always exists)'.format(email))
                messages.error(request, 'User with email: <b>{}</b> always exists'.format(email))
            
            else: 
                Partner.objects.create(phone=phone, address=address, 
                                       legal_name=legal_name, user=user)

                logger.debug('Registered partner with email {!r}'.format(user.email))

                return redirect('/login')
            
        else: 
            logger.debug('Recieved invalid form')
            flash_form_errors(request, form)

    if request.user.is_authenticated(): 
        return redirect('/dashboard')

    return render(request, 'registration/registration.html')