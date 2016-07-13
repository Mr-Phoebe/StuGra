from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
	list_display = ('teaid','name','sex','birth')
	def get_readonly_fields(self,request,obj=None):
		if not request.user.is_superuser:
			return [f.name for f in self.model._meta.fields]
		return self.readonly_fields
	def get_queryset(self, request):
		qs = super(TeacherAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(teaid=int(request.user.first_name))

admin.site.register(Teacher,TeacherAdmin)

# Register your models here.
