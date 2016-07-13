#coding: utf-8
from django.db import models

class Teacher(models.Model):
	SEX_CHOICES = (
        (u'男', u'男'),
        (u'女', u'女'),
    )

	teaid = models.PositiveIntegerField(u'教师编号',primary_key=True)
	name = models.CharField(u'姓名',max_length=10)
	sex = models.CharField(u'性别',choices=SEX_CHOICES,default=u'男',max_length=2)
	birth = models.DateField(u'生日',blank=True)
	def __unicode__(self):
		return str(self.teaid)
	class Meta:
		verbose_name = u'教师'
		verbose_name_plural = u'教师'

# Create your models here.
