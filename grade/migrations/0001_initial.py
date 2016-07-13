# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20150714_0113'),
        ('course', '0004_auto_20150714_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.PositiveIntegerField(verbose_name='\u5206\u6570')),
                ('cid', models.ForeignKey(to='course.Course')),
                ('sid', models.ForeignKey(to='student.Student')),
            ],
            options={
                'verbose_name': '\u6210\u7ee9',
                'verbose_name_plural': '\u6210\u7ee9',
            },
        ),
    ]
