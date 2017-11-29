# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0021_auto_20171129_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='genres', to='films.Genre'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Movie'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Movie'),
        ),
    ]
