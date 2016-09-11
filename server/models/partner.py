from django.contrib.auth.base_user import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField as PhoneField
from django.db.models import Model, EmailField, CharField, OneToOneField
from django.contrib.auth.models import User



class Partner(Model): 
    user       = OneToOneField(User)
    legal_name = CharField(max_length=120)
    phone      = PhoneField(blank=True)
    address    = CharField(max_length=120)

    def __str__(self): 
        return str(self.user.name)