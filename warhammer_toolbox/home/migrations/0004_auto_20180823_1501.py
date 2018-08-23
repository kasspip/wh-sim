# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-23 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180819_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegressiveProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('life_1', models.CharField(choices=[(b'0', b'-'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30')], default=b'0', max_length=32)),
                ('life_2', models.CharField(choices=[(b'0', b'-'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30')], default=b'0', max_length=32)),
                ('life_3', models.CharField(choices=[(b'0', b'-'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30')], default=b'0', max_length=32)),
                ('movement_1', models.CharField(choices=[(b'0', b'-'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12')], default=b'0', max_length=32)),
                ('movement_2', models.CharField(choices=[(b'0', b'-'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12')], default=b'0', max_length=32)),
                ('movement_3', models.CharField(choices=[(b'0', b'-'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12')], default=b'0', max_length=32)),
                ('melee_1', models.CharField(choices=[(b'0', b'-'), (b'1', b'1+'), (b'2', b'2+'), (b'3', b'3+'), (b'4', b'4+'), (b'5', b'5+'), (b'6', b'6+')], default=b'0', max_length=32)),
                ('melee_2', models.CharField(choices=[(b'0', b'-'), (b'1', b'1+'), (b'2', b'2+'), (b'3', b'3+'), (b'4', b'4+'), (b'5', b'5+'), (b'6', b'6+')], default=b'0', max_length=32)),
                ('melee_3', models.CharField(choices=[(b'0', b'-'), (b'1', b'1+'), (b'2', b'2+'), (b'3', b'3+'), (b'4', b'4+'), (b'5', b'5+'), (b'6', b'6+')], default=b'0', max_length=32)),
                ('range_1', models.CharField(choices=[(b'0', b'-'), (b'1', b'1+'), (b'2', b'2+'), (b'3', b'3+'), (b'4', b'4+'), (b'5', b'5+'), (b'6', b'6+')], default=b'0', max_length=32)),
                ('range_2', models.CharField(choices=[(b'0', b'-'), (b'1', b'1+'), (b'2', b'2+'), (b'3', b'3+'), (b'4', b'4+'), (b'5', b'5+'), (b'6', b'6+')], default=b'0', max_length=32)),
                ('range_3', models.CharField(choices=[(b'0', b'-'), (b'1', b'1+'), (b'2', b'2+'), (b'3', b'3+'), (b'4', b'4+'), (b'5', b'5+'), (b'6', b'6+')], default=b'0', max_length=32)),
                ('attacks_1', models.CharField(choices=[(b'0', b'-'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'D3', b'D3'), (b'2D3', b'2D3'), (b'3D3', b'3D3'), (b'D6', b'D6'), (b'2D6', b'2D6'), (b'3D6', b'3D6')], default=b'0', max_length=32)),
                ('attacks_2', models.CharField(choices=[(b'0', b'-'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'D3', b'D3'), (b'2D3', b'2D3'), (b'3D3', b'3D3'), (b'D6', b'D6'), (b'2D6', b'2D6'), (b'3D6', b'3D6')], default=b'0', max_length=32)),
                ('attacks_3', models.CharField(choices=[(b'0', b'-'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'D3', b'D3'), (b'2D3', b'2D3'), (b'3D3', b'3D3'), (b'D6', b'D6'), (b'2D6', b'2D6'), (b'3D6', b'3D6')], default=b'0', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='degressive_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='base_profiles', to='home.DegressiveProfile'),
        ),
    ]
