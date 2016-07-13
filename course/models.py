#coding: utf-8
from django.db import models

class Course(models.Model):
	verbose_name = u'课程'

	MASTER_CHOICES = (
        (u'春季', u'春季'),
        (u'秋季', u'秋季'),
    )

	TYPE_CHOICES = (
        (u'选修', u'选修'),
        (u'必修', u'必修'),
    )

	cid = models.PositiveIntegerField(u'课程号',primary_key=True)
	name = models.CharField(u'课程名',max_length=10)
	credit = models.PositiveIntegerField(u'学分')
	master = models.CharField(u'学期',choices=MASTER_CHOICES,default=u'春季',max_length=2)
	ctype = models.CharField(u'类型',choices=TYPE_CHOICES,default=u'必修',max_length=2)

	def __unicode__(self):
		return (u'%s-%s' % (str(self.cid), self.name))
	class Meta:
		verbose_name = u'课程'
		verbose_name_plural = u'课程'

# Create your models here.
