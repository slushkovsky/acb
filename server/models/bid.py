import datetime

from django.conf import settings
from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField as PhoneField
from django.db.models import Model, TimeField, DateField, CharField, \
                             OneToOneField
                             
from .instructor import Instructor


class Bid(Model): 
    class Meta: 
        verbose_name        = _('Bid')
        verbose_name_plural = _('Bids')
    
    date       = DateField (_('Date'      ))
    begin_time = TimeField (_('Begin time'))
    end_time   = TimeField (_('End time'  ))
    name       = CharField (_('Name'      ), max_length=20)
    phone      = PhoneField(_('Phone'     ))

    instructor = OneToOneField(Instructor, verbose_name=_('Instructor'))


    def __str__(self): 
    	return '{begin} - {end} {date}, {name}'.format(
            date =self.date      .strftime(settings.DATE_STR_FORMAT),
            begin=self.begin_time.strftime(settings.TIME_STR_FORMAT),
            end  =self.end_time  .strftime(settings.TIME_STR_FORMAT),
            name =str(self.instructor)
        )