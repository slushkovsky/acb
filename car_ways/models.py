from django.db import models
from django.contrib import settings
from django.utils.translation import ugettext as _ 
from pymongo import MongoClient


__working_hours = MongoClient()[settings.APP_MONGO_DB][settings.MONGO_WORK_HOURS_COLLECITON]


class Bid(models.Model): 
    class Meta: 
        verbose_name        = _('Bid')
        verbose_name_plural = _('Bids')


    instructor = models.OneToOneField(Instructor, verbose_name=_('Instructor'))
    datetime_from = models.DateTimeField(_('From'))
    datetime_to = models.DateTimeField(_('To'))




class Car(models.Model):
    class Meta:
        verbose_name        = _('Car')
        verbose_name_plural = _('Cars')
    
    mark  = models.CharField(_('Mark'),  max_length=20)
    model = models.CharField(_('Model'), max_length=30)

    GEAR_BOX_CHOICES = (
        ('mech', _('Machanical')),
        ('auto', _('Automotive'))
    )

    gear_box = models.CharField(_('PPC'), max_length=20, choices=GEAR_BOX_CHOICES)
    
    photo = models.ImageField(_('Photo'), null=True, blank=True)


    def __str__(self): 
        return '{mark} {model}'.format(mark=self.mark, model=self.model)



class City(models.Model): 
    class Meta: 
        verbose_name        = _('City')
        verbose_name_plural = _('Cities')

    
    name = models.CharField(_('Name'), max_length=30)


    def __str__(self): 
        return self.name



class District(models.Model): 
    class Meta: 
        verbose_name        = _('District')
        verbose_name_plural = _('Districts')


    city = models.OneToOneField(City, verbose_name=_('City'))
    name = models.CharField(_('Name'), max_length=40)

    def __str__(self): 
        return self.name



class Waybill(models.Model):
    class Meta:
        verbose_name        = _('Waybill')
        verbose_name_plural = _('Waybills')


    area = models.OneToOneField(District, verbose_name=_('District'))
    schema = models.ImageField(_('Schema'))


    def __str__(self): 
        return self.area.name



class Instructor(models.Model):
    class Meta:
        verbose_name        = _('Instructor')
        verbose_name_plural = _('Instructors')


    name             = models.CharField   (_('First name'),  max_length=50)
    surname          = models.CharField   (_('Last urname'), max_length=50)
    patronymic       = models.CharField   (_('Patronymic'),  max_length=50)
    photo            = models.ImageField  (_('Photo'), null=True, blank=True)
    with_licence     = models.BooleanField(_('With license'))
    with_limitations = models.BooleanField(_('With limitations'))

    car              = models.OneToOneField(Car, verbose_name=_('Car'))
    waybills         = models.ManyToManyField(Waybill, verbose_name=_('Waybills'))


    def __str__(self):
        return '{name} {patronymic} {surname}'.format(name      =self.name,
                                                      surname   =self.surname,
                                                      patronymic=self.patronymic) 


    def set_working_hours(self, date, hours):
        user_hours = __working_hours.get(self.id, {})
        date_key = date.strftime(settings.MONGO_DATE_FORMAT)

        user_hours.insert_one(data_key, [{
            'from': hours_range.begin.strftime(settings.MONGO_TIME_FORMAT),
            'to':   hours_range.end  .strftime(settings.MONGO_TIME_FORMAT)} for hours_range in hours])


    def get_working_hours(self, date):
        user_hours = mongo[settings.MONGO_WORK_HOURS_COLLECITON][self.id]
        hours = user_hours[date.strftime(settings.MONGO_DATE_FORMAT)]

        return hours



