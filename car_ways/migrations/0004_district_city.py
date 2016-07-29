# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_ways', '0003_auto_20160729_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='city',
            field=models.OneToOneField(default=-1, on_delete=django.db.models.deletion.CASCADE, to='car_ways.City'),
            preserve_default=False,
        ),
    ]
