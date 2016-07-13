from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ('stuid','name','sex','birth')
	def get_readonly_fields(self,request,obj=None):
		if not request.user.is_superuser:
			return [f.name for f in self.model._meta.fields]
		return self.readonly_fields
	def get_queryset(self, request):
		qs = super(StudentAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(stuid=int(request.user.first_name))
	#readonly_fields = ('stuid',)
	#list_filter = ('stuid',)

admin.site.register(Student,StudentAdmin)

# Register your models here.
