# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-24 13:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180823_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='degressive_profile',
            new_name='degressive',
        ),
    ]
