# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20161211_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='state',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='street',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
