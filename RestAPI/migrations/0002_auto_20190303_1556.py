# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-03 15:56
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weather',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='location',
            name='temperature',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
