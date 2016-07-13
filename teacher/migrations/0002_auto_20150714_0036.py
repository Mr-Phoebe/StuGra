# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.CharField(default='\u7537', max_length=2, verbose_name='\u6027\u522b', choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')]),
        ),
    ]
