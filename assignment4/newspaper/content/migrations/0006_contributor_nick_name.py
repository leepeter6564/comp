# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-19 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20160319_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='nick_name',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]