#coding: utf-8
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
	list_display = ('cid','name','credit','master','ctype')

	#fieldsets = (
    #    ('基本信息', {'fields': ('cid', 'name')}),
    #    ('Meta Data', {'fields': ('credit', 'master', 'ctype')}),
    #)

	#suit_form_tabs = (('hello','hello'),('test','test'))

	#suit_form_includes = (
    #    ('admin/course/course/chart.html','','test'),
    #)

admin.site.register(Course,CourseAdmin)

# Register your models here.
