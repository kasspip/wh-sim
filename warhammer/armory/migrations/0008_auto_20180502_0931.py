# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-02 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('armory', '0007_auto_20180502_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('icon', models.ImageField(null=True, upload_to='Faction')),
            ],
        ),
        migrations.AddField(
            model_name='figurine',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='figurines', to='armory.Role'),
        ),
    ]
