# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170313_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='cover',
            field=models.ImageField(default=None, upload_to='covers/'),
            preserve_default=False,
        ),
    ]
