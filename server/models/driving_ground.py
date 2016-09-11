from django.db.models import Model, ForeignKey, ImageField, CharField

from .geo import District


class DrivingGround(Model):
	district = ForeignKey(District)
	address  = CharField(max_length=120)
	photo    = ImageField(blank=True)

	def __str__(self): 
		return self.address