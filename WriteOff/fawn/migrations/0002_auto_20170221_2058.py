# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fawn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='full_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]