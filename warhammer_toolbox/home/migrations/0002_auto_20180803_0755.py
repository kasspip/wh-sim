# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-03 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figurine',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='figurines'),
        ),
    ]
