from django.db import models
from django.utils.translation import ugettext as _

from .geo import District


class Waybill(models.Model):
    class Meta:
        verbose_name        = _('Waybill')
        verbose_name_plural = _('Waybills')

    area = models.OneToOneField(District, verbose_name=_('District'))
    schema = models.ImageField(_('Schema'))

    def __str__(self): 
        return self.area.name