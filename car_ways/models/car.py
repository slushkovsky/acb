from django.db import models
from django.utils.translation import ugettext as _


class Car(models.Model):
    class Meta:
        verbose_name        = _('Car')
        verbose_name_plural = _('Cars')
    

    GEAR_BOX_CHOICES = (
        ('mech', _('Machanical')),
        ('auto', _('Automotive'))
    )

    mark     = models.CharField (_('Mark'    ), max_length=20)
    model    = models.CharField (_('Model'   ), max_length=30)
    gear_box = models.CharField (_('Gear box'), max_length=20, choices=GEAR_BOX_CHOICES)
    photo    = models.ImageField(_('Photo'   ), null=True, blank=True)

    def __str__(self): 
        return '{mark} {model}'.format(mark=self.mark, model=self.model)