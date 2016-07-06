from django.db import models

# Create your models here.


class Car(models.Model):
    mark = models.CharField('Марка', max_length=20)
    model = models.CharField('Модель', max_length=30)

    GEAR_BOX_CHOICES = (
        ('mech', 'Механическая'),
        ('auto', 'Автоматическая')
    )
    gear_box = models.CharField('Коробка передач', max_length=20, choices=GEAR_BOX_CHOICES)
    photo = models.ImageField('Фото', null=True, blank=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Waybill(models.Model):
    area = models.CharField('Район', max_length=80)
    schema = models.ImageField('Схема')

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


class Employe(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)

    car = models.OneToOneField(Car, verbose_name='Авто')
    waybills = models.ManyToManyField(Waybill, verbose_name='Маршруты')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
