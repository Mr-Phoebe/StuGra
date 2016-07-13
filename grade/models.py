#coding: utf-8
from django.db import models
from student.models import Student
from course.models import Course

class Grade(models.Model): #定义Grade表
	sid = models.ForeignKey(Student,verbose_name=u'学生')
	cid = models.ForeignKey(Course,verbose_name=u'课程')
	mark = models.PositiveIntegerField(u'分数')

	def __unicode__(self): #重载Grade在路径中的名称
		return u'成绩详情'
	class Meta: #重载Grade在菜单中的名称
		verbose_name = u'成绩'
		verbose_name_plural = u'成绩'
		

# Create your models here.
