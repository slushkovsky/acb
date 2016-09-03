from django.db import models 
from django.conf import settings
from django.utils.translation import ugettext as _ 

WEEK_DAYS_CHOICES = (
    (1, _('Monday'   )),
    (2, _('Tuesday'  )),
    (3, _('Wednesday')),
    (4, _('Thursday' )),
    (5, _('Friday'   )),
    (6, _('Saturday' )),
    (7, _('Sunday'   ))
)


class InstantRest(models.Model):
	class Meta: 
		verbose_name        = _('Instant rest')
		verbose_name_plural = _('Instant rests')


	day_of_week = models.IntegerField(_('Day of week'), choices=WEEK_DAYS_CHOICES)
	time_from   = models.TimeField   (_('Time from'))
	time_to     = models.TimeField   (_('Time to'))

	def __str__(self): 
		dayname = [day for day in WEEK_DAYS_CHOICES if day[0] == self.day_of_week][0]

		return '{day}, {begin} - {end}'.format(day  =dayname,
			                                   begin=time_from,
			                                   end  =time_to);


class SingleRest(models.Model): 
	class Meta: 
		verbose_name        = _('Single rest')
		verbose_name_plural = _('Single rests')


	begin = models.DateTimeField(_('Begin'))
	end   = models.DateTimeField(_('End'))


	def __str__(self): 
		return '{begin} - {end}'.format(
			begin=self.begin.strftime(settings.DATETIME_STR_FORMAT),
			end  =self.end  .strftime(settings.DATETIME_STR_FORMAT)
		)