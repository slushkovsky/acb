# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_ways', '0002_auto_20160729_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='waybill',
            name='area',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car_ways.District'),
        ),
    ]
