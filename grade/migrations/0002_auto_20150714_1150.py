# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='cid',
            field=models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='course.Course'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='sid',
            field=models.ForeignKey(verbose_name='\u5b66\u751f', to='student.Student'),
        ),
    ]
