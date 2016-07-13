# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20150713_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(max_length=2, verbose_name='\u6027\u522b', choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')]),
        ),
        migrations.DeleteModel(
            name='Sex',
        ),
    ]
