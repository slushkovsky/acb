from django.forms import ModelForm, Form, CharField, EmailField

from .models import Partner


class RegisterForm(ModelForm):
	class Meta: 
		model = Partner
		fields = ['email', 'name', 'ligal_type', 'phone', 'password']

class LoginForm(ModelForm): 
	email    = EmailField()
	password = CharField(max_length=100)