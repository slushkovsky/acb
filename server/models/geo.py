from django.db.models import Model, CharField, OneToOneField
from django.utils.translation import ugettext as _


class City(Model): 
    class Meta: 
        verbose_name        = _('City')
        verbose_name_plural = _('Cities')
    
    name = CharField(_('Name'), max_length=30)

    def __str__(self): 
        return self.name


class District(Model): 
    class Meta: 
        verbose_name        = _('District')
        verbose_name_plural = _('Districts')

    city = OneToOneField(City, verbose_name=_('City'))
    name = CharField(_('Name'), max_length=40)

    def __str__(self): 
        return self.name