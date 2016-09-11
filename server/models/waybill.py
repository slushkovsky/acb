from django.db.models import Model, OneToOneField, ImageField
from django.utils.translation import ugettext as _

from .geo import District


class Waybill(Model):
    class Meta:
        verbose_name        = _('Waybill')
        verbose_name_plural = _('Waybills')


    schema = ImageField(_('Schema'))
    area = OneToOneField(District, verbose_name=_('District'))

    def __str__(self): 
        return str(self.area.name)