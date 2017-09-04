# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-04 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20170904_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='avg_rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='contact',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='hospitalrating',
            name='google_rating',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]