from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.forms import Form, EmailField, CharField
from django.contrib import messages
from emailusernames.utils import create_user

from server.models import Partner
from django.contrib.auth.models import User
from server.utils import flash_form_errors


class RegistrationFrom(Form): 
    official_name = CharField() 
    address       = CharField()
    phone         = CharField(required=False)
    email         = EmailField()
    password      = CharField()


@require_http_methods(['GET', 'POST'])
def registration_view(request): 
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)

        if form.is_valid(): 
            try: 
                user = create_user(email   =form.cleaned_data['email'],
                                   password=form.cleaned_data['password'])
            except AttributeError as e: 
                messages.error(request, 'User with email: <b>{}</b> always exists'.format(form.cleaned_data['email']))
            else: 
                partner= Partner(phone        =form.cleaned_data['phone'], 
                                 address      =form.cleaned_data['address'],
                                 official_name=form.cleaned_data['official_name'],
                                 user         =user)
                partner.save()
            
        else: 
            flash_form_errors(request, form)

    return render(request, 'registration/registration.html')