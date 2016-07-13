# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20150714_0036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '\u6559\u5e08', 'verbose_name_plural': '\u6559\u5e08'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teaid',
            field=models.PositiveIntegerField(serialize=False, verbose_name='\u6559\u5e08\u7f16\u53f7', primary_key=True),
        ),
    ]
