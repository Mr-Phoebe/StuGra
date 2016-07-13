#coding: utf-8
from django.db import models

class Classes(models.Model):
	cid = models.PositiveIntegerField(u'班级号',primary_key=True)
	major = models.CharField(u'专业',max_length=10)
	def __unicode__(self):
		return str(self.cid)
	class Meta:
		verbose_name = u'班级'
		verbose_name_plural = u'班级'

# Create your models here.