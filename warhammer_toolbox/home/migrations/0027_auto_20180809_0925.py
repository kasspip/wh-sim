# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-09 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20180807_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='home.Unit'),
        ),
    ]
