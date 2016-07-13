# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teaid', models.IntegerField(serialize=False, verbose_name='\u6559\u5e08\u7f16\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u59d3\u540d')),
                ('sex', models.CharField(max_length=2, verbose_name='\u6027\u522b')),
                ('birth', models.DateField(verbose_name='\u751f\u65e5', blank=True)),
            ],
        ),
    ]
