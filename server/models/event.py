from django.utils.translation import ugettext as _ 
from django.db.models import Model, CharField, DateField, TimeField, \
                             IntegerField, ManyToManyField

from server.models import Instructor


class Event(Model): 
	name = CharField(max_length=120, blank=True)
	descr = CharField(max_length=300, blank=True)
	
	partisipants = ManyToManyField(Instructor)

	date = DateField()
	time_from = TimeField()
	time_to = TimeField()

	repeat_period = IntegerField(blank=True) # In days
	repeat_end = IntegerField(blank=True)

	def __str__(self): 
		return '{data} {time_from}-{time_to}'.format(**vars(self))


