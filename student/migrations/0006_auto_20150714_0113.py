# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20150714_0036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u5b66\u751f', 'verbose_name_plural': '\u5b66\u751f'},
        ),
        migrations.AlterField(
            model_name='student',
            name='stuid',
            field=models.PositiveIntegerField(serialize=False, verbose_name='\u5b66\u53f7', primary_key=True),
        ),
    ]
