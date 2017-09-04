# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-04 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hospital',
            options={'ordering': ['-avg_rating']},
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='beds',
        ),
        migrations.AddField(
            model_name='hospital',
            name='avg_rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
            preserve_default=False,
        ),
    ]
