from django.db import models

class Car(models.Model):
    mark = models.CharField('Mark', max_length=20)
    model = models.CharField('Model', max_length=30)

    GEAR_BOX_CHOICES = (
        ('mech', 'Machanical'),
        ('auto', 'Automotive')
    )
    gear_box = models.CharField('PPC', max_length=20, choices=GEAR_BOX_CHOICES)
    
    photo = models.ImageField('Photos', null=True, blank=True)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Waybill(models.Model):
    area = models.CharField('District', max_length=80)
    schema = models.ImageField('Schema')

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'


class Employe(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)

    car = models.OneToOneField(Car, verbose_name='car')
    waybills = models.ManyToManyField(Waybill, verbose_name='routes')

    class Meta:
        verbose_name = 'Employe'
        verbose_name_plural = 'Employees'