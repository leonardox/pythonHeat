# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-01 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.CharField(default='pedo', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=b'documents/'),
        ),
    ]