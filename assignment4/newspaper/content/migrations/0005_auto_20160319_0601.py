# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-19 06:01
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20160319_0459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='nick_name',
        ),
        migrations.AddField(
            model_name='article',
            name='post_script',
            field=tinymce.models.HTMLField(default=b''),
        ),
    ]
