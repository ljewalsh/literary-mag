# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_issue_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='/submissions')),
            ],
        ),
        migrations.CreateModel(
            name='Submitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='issue',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Issue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='submitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Submitter'),
        ),
    ]
