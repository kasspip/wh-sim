# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-06 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20180806_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='figurine',
            old_name='faction',
            new_name='army',
        ),
    ]
