# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 05:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0014_auto_20160121_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='tym',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 10, 42, 52, 325625)),
        ),
    ]