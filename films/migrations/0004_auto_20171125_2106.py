# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20171125_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='name',
        ),
    ]
