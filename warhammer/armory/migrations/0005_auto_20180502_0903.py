# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-02 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0004_squad_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faction',
            name='icon',
            field=models.ImageField(null=True, upload_to='Faction'),
        ),
    ]