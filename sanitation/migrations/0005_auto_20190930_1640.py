# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-30 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanitation', '0004_auto_20190928_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='phone_Number',
            field=models.CharField(max_length=15),
        ),
    ]