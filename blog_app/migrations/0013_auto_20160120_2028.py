# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='pst',
        ),
        migrations.AddField(
            model_name='comments',
            name='slug',
            field=models.CharField(default='', max_length=255),
        ),
    ]
