# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jcms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
