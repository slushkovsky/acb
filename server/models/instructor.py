from django.utils.translation import ugettext as _ 
from phonenumber_field.modelfields import PhoneNumberField as PhoneField
from django.db.models import Model, CharField, ImageField, \
                             BooleanField, ForeignKey, \
                             ManyToManyField, EmailField

from .car import Car
from .waybill import Waybill


class Instructor(Model):
    class Meta:
        verbose_name        = _('Instructor')
        verbose_name_plural = _('Instructors')

    first_name       = CharField   (_('First name'), max_length=50)
    last_name        = CharField   (_('Last name'), max_length=50)
    photo            = ImageField  (_('Photo'), null=True, blank=True)
    with_license     = BooleanField(_('With license'))
    with_limitations = BooleanField(_('With limitations'))
    phone            = PhoneField  (_('Phone'))
    email            = EmailField  (_('Email'))
    car              = ForeignKey(Car)
    waybills         = ManyToManyField(Waybill,     verbose_name=_('Waybills'    ))
    
    def __str__(self):
        return '{first_name} {last_name}'.format(**vars(self)) 

