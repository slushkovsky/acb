from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
import datetime

from .instructor import Instructor
from car_ways import validators


class Bid(models.Model): 
    class Meta: 
        verbose_name        = _('Bid')
        verbose_name_plural = _('Bids')
    
    date       = models.DateField(_('Date'      ))
    begin_time = models.TimeField(_('Begin time'))
    end_time   = models.TimeField(_('End time'  ))
    name       = models.CharField(_('Name'      ), max_length=20)
    phone      = models.CharField(_('Phone'     ), max_length=17, validators=[validators.PHONE])

    instructor    = models.OneToOneField(Instructor, verbose_name=_('Instructor'))


    def __str__(self): 
    	return '{begin} - {end} {date}, {name}'.format(
            date =self.date      .strftime(settings.DATE_STR_FORMAT),
            begin=self.begin_time.strftime(settings.TIME_STR_FORMAT),
            end  =self.end_time  .strftime(settings.TIME_STR_FORMAT),
            name =str(self.instructor)
        )