from django import forms
from .models import students, event
class regi(forms.ModelForm):
	class Meta:
		model=students
		#fields='__all__'
		exclude = ('Attendance',)


class add_event(forms.ModelForm):
	class Meta:
		model=event
		#fields='__all__'
		exclude = ('total_seats','is_done')

#class login(forms.ModelForm):
	#class meta:
		#field='__all__'