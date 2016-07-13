#coding: utf-8
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Grade

# 定义用户访问Grade后的操作
class GradeAdmin(admin.ModelAdmin):
	list_display = ('sid','cid','mark')
	def get_readonly_fields(self,request,obj=None):
		if not request.user.is_superuser:
			if cmp(request.user.last_name,'teacher'):
				return [f.name for f in self.model._meta.fields]
			else:
				tl = [f.name for f in self.model._meta.fields]
				del tl[tl.index('mark')]
				return tl
		return self.readonly_fields
	def get_queryset(self, request):
		qs = super(GradeAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		elif cmp(request.user.last_name,'teacher'):
			return qs.filter(sid__stuid=int(request.user.first_name))
		else:
			return qs
	#list_filter = ('sid',)

admin.site.register(Grade,GradeAdmin)

# Register your models here.
