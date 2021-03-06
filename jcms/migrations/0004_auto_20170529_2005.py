# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jcms', '0003_remove_option_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='code',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='option',
            unique_together=set([('type', 'value')]),
        ),
    ]
