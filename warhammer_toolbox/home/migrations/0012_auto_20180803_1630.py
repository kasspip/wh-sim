# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-03 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20180803_1625'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='figurine',
            name='avatar',
        ),
    ]
