# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0011_auto_20171127_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tmdbID',
            field=models.IntegerField(null=True),
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
