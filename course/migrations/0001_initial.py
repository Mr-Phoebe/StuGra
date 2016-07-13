# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.IntegerField(serialize=False, verbose_name='\u8bfe\u7a0b\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u8bfe\u7a0b\u540d')),
                ('credit', models.IntegerField(default=1, verbose_name='\u5b66\u5206')),
                ('master', models.CharField(default='\u6625\u5b63', max_length=2, verbose_name='\u5b66\u671f', choices=[('\u6625\u5b63', '\u6625\u5b63'), ('\u79cb\u5b63', '\u79cb\u5b63')])),
                ('ctype', models.CharField(default='\u5fc5\u4fee', max_length=2, verbose_name='\u7c7b\u578b', choices=[('\u9009\u4fee', '\u9009\u4fee'), ('\u5fc5\u4fee', '\u5fc5\u4fee')])),
            ],
        ),
    ]
