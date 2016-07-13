# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cid',
            field=models.PositiveIntegerField(serialize=False, verbose_name='\u8bfe\u7a0b\u53f7', primary_key=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='credit',
            field=models.PositiveIntegerField(verbose_name='\u5b66\u5206'),
        ),
    ]
