# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fawn', '0002_auto_20170221_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='type',
            new_name='file_type',
        ),
    ]
