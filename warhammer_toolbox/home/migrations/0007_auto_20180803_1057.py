# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-03 10:57
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180803_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figurine',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('picture', '256x256', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
