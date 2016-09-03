from django.db.models import Model, CharField, ImageField
from django.utils.translation import ugettext as _


class Car(Model):
    class Meta:
        verbose_name        = _('Car')
        verbose_name_plural = _('Cars')
    

    GEAR_BOX = (
        ('mech', _('Machanical')),
        ('auto', _('Automotive'))
    )

    mark     = CharField (_('Mark'    ), max_length=20)
    model    = CharField (_('Model'   ), max_length=30)
    gear_box = CharField (_('Gear box'), max_length=20, choices=GEAR_BOX)
    photo    = ImageField(_('Photo'   ), null=True, blank=True)

    def __str__(self): 
        return '{mark} {model}'.format(mark =self.mark, 
                                       model=self.model)