# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_ways', '0005_auto_20160729_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('with_licence', models.BooleanField()),
                ('with_limitations', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Инструктор',
                'verbose_name_plural': 'Инструктора',
            },
        ),
        migrations.RemoveField(
            model_name='employe',
            name='car',
        ),
        migrations.RemoveField(
            model_name='employe',
            name='waybills',
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'Район', 'verbose_name_plural': 'Районы'},
        ),
        migrations.AlterModelOptions(
            name='waybill',
            options={'verbose_name': 'Маршрут', 'verbose_name_plural': 'Маршруты'},
        ),
        migrations.AlterField(
            model_name='car',
            name='gear_box',
            field=models.CharField(choices=[('mech', 'Механическая'), ('auto', 'Автоматическая')], max_length=20, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='car',
            name='mark',
            field=models.CharField(max_length=20, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=30, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='district',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car_ways.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='waybill',
            name='area',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car_ways.District', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='waybill',
            name='schema',
            field=models.ImageField(upload_to='', verbose_name='Схема'),
        ),
        migrations.DeleteModel(
            name='Employe',
        ),
        migrations.AddField(
            model_name='instructor',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car_ways.Car', verbose_name='Машина'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='waybills',
            field=models.ManyToManyField(to='car_ways.Waybill', verbose_name='Маршруты'),
        ),
    ]
