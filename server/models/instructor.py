from django.utils.translation import ugettext as _ 
from phonenumber_field.modelfields import PhoneNumberField as PhoneField
from django.db.models import Model, CharField, ImageField, \
                             BooleanField, OneToOneField,  \
                             ManyToManyField, EmailField

from .car import Car
from .waybill import Waybill
from .rest import SingleRest, InstantRest


class Instructor(Model):
    class Meta:
        verbose_name        = _('Instructor')
        verbose_name_plural = _('Instructors')


    first_name       = CharField   (_('First name'), max_length=50)
    last_name        = CharField   (_('Last name'), max_length=50)
    photo            = ImageField  (_('Photo'), null=True, blank=True)
    with_licence     = BooleanField(_('With license'))
    with_limitations = BooleanField(_('With limitations'))
    phone            = PhoneField  (_('Phone'))
    email            = EmailField  (_('Email'))

    car              = OneToOneField  (Car,         verbose_name=_('Car'         ))
    waybills         = ManyToManyField(Waybill,     verbose_name=_('Waybills'    ))
    instant_rest     = ManyToManyField(InstantRest, verbose_name=_('Instant rest'))
    single_rest      = ManyToManyField(SingleRest,  verbose_name=_('Single rest' ))

    def __str__(self):
        return '{name} {surname}'.format(name   =self.name,
                                         surname=self.surname) 

