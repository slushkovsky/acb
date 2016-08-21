from django.db import models
from django.utils.translation import ugettext as _


class City(models.Model): 
    class Meta: 
        verbose_name        = _('City')
        verbose_name_plural = _('Cities')
    
    name = models.CharField(_('Name'), max_length=30)

    def __str__(self): 
        return self.name


class District(models.Model): 
    class Meta: 
        verbose_name        = _('District')
        verbose_name_plural = _('Districts')

    city = models.OneToOneField(City, verbose_name=_('City'))
    name = models.CharField(_('Name'), max_length=40)

    def __str__(self): 
        return self.name