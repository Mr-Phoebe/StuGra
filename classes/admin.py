#coding:utf-8
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Classes

class ClassesAdmin(admin.ModelAdmin):
	list_display = ('cid','major')

admin.site.register(Classes,ClassesAdmin)
