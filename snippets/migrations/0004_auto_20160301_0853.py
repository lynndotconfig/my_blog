# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-01 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20160301_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='samplesheet',
            field=models.FileField(blank=True, default='', upload_to='snippets/uploads/%Y/%m/%d'),
        ),
    ]
