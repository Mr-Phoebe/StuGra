# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.ForeignKey(to='student.Sex'),
        ),
    ]
