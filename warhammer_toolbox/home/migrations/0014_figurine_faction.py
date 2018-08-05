# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-05 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20180805_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='figurine',
            name='faction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='figurines', to='home.Faction'),
        ),
    ]