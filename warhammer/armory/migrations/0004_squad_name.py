# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-02 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0003_auto_20180502_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='name',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
