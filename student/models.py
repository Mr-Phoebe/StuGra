#coding: utf-8
from django.db import models

class Student(models.Model):
	SEX_CHOICES = (
        (u'男', u'男'),
        (u'女', u'女'),
    )

	stuid = models.PositiveIntegerField(u'学号',primary_key=True)
	name = models.CharField(u'姓名',max_length=10)
	sex = models.CharField(u'性别',choices=SEX_CHOICES,default=u'男',max_length=2)
	birth = models.DateField(u'生日',blank=True)

	def __unicode__(self):
		return (u'%s-%s' % (str(self.stuid), self.name))
	class Meta:
		verbose_name = u'学生'
		verbose_name_plural = u'学生'

# Create your models here.
