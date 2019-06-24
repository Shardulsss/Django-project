from django.contrib import admin
from .models import event,students,User
from django.contrib.auth.models import Group

admin.site.site_header= 'Admin '

def attend_action(modeladmin, request, queryset):
	for students in queryset:
		students.Attendance = True
		students.save()

attend_action.description = 'Attended'			

class studentsAdmin(admin.ModelAdmin):
	list_display = ('student_name','Branch','year','clgId','name','Attendance')
	list_filter = ('Branch','year','name','Attendance')
	search_fields = ['student_name','Branch','clgId']
	actions = [attend_action,]

class eventAdmin(admin.ModelAdmin):
	list_display = ('name','place','day','no_of_seats')
	list_filter = ['place']
	search_fields = ['name']

admin.site.register(event,eventAdmin)
admin.site.register(students,studentsAdmin)
admin.site.register(User)