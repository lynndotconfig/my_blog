# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-15 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import snippets.models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20160307_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='samplesheet',
            field=models.FileField(blank=True, default='', upload_to='snippets/uploads/%Y/%m/%d', validators=[snippets.models.validate_file]),
        ),
    ]