# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-20 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jcms', '0004_auto_20170529_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='setting',
            unique_together=set([('type', 'value')]),
        ),
    ]
