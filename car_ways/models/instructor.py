from django.db import models
from django.utils.translation import ugettext as _ 

from .car import Car
from .waybill import Waybill
from .rest import SingleRest, InstantRest


class Instructor(models.Model):
    class Meta:
        verbose_name        = _('Instructor')
        verbose_name_plural = _('Instructors')


    name             = models.CharField   (_('First name'),  max_length=50)
    surname          = models.CharField   (_('Last urname'), max_length=50)
    patronymic       = models.CharField   (_('Patronymic'),  max_length=50)
    photo            = models.ImageField  (_('Photo'), null=True, blank=True)
    with_licence     = models.BooleanField(_('With license'))
    with_limitations = models.BooleanField(_('With limitations'))

    car              = models.OneToOneField  (Car,         verbose_name=_('Car'         ))
    waybills         = models.ManyToManyField(Waybill,     verbose_name=_('Waybills'    ))
    instant_rest     = models.ManyToManyField(InstantRest, verbose_name=_('Instant rest'))
    single_rest      = models.ManyToManyField(SingleRest,  verbose_name=_('Single rest' ))

    def __str__(self):
        return '{name} {surname}'.format(name   =self.name,
                                         surname=self.surname) 

