# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-03 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanitation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpesacallbacks',
            name='checkout_request_id',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='mpesacallbacks',
            name='merchant_id',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='mpesacalls',
            name='checkout_request_id',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='mpesacalls',
            name='merchant_id',
            field=models.TextField(default=''),
        ),
    ]