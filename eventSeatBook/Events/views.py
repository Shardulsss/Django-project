from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import event,students,User
from .forms import regi, add_event
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def events(request):
	alb = event.objects.filter(is_done = False)
	return render(request, 'Events/index.html',{'alb': alb})
def dete(request,id):
#alb = event.objects.all()
	albu = get_object_or_404(event, id=id)
	return render(request, 'Events/evinfo.html',{'albu':albu})

def delete_event(request,id):
#alb = event.objects.all()
	event_this = get_object_or_404(event, id=id)
	students_all = students.objects.filter(name=event_this, Attendance=False)
	students_attended = students.objects.filter(name=event_this, Attendance=True)
	return render(request, 'Events/eventdelete.html',{'event':event_this, 'student':students_all, 'std':students_attended})


def deletor(request,id):
	event_this = get_object_or_404(event, id=id)
	event_this.delete()
	return HttpResponse("<h1>deleted</h1>")

def updater(request,id):
	event_this = get_object_or_404(event, id=id)
	event_this.is_done = True
	event_this.save()
	return HttpResponse("<h1>Updated</h1>")

def presenter(request,id):
	student_this = get_object_or_404(students, id=id)
	student_this.Attendance = True
	student_this.save()
	return HttpResponse("<h1>Updated</h1>")

def adminpage(request):
	events_all = event.objects.all()
	students_all = students.objects.all()
	branchchoice=['INFT','COMPS','CIVIL','MECH','INST']
	yearchoice=['FE','SE','TE','BE']
	return render(request, 'Events/adminhtml.html',{'events':events_all , 'student':students_all,'brchoice':branchchoice,'yrchoice':yearchoice})

#def stdlist(request):
#alb = event.objects.all()
	#event_this = get_object_or_404(event, id=id)
	#return render(request, 'Events/stdlist.html',{'event':event_this})

class stdlist(generic.ListView):
	template_name='Events/stdlist.html'

	def get_queryset(self):
		return students.objects.filter(Branch=self.kwargs['Branch'])
		
class stdlistt(generic.ListView):
	template_name='Events/stdlist2.html'

	def get_queryset(self):
		return students.objects.filter(year=self.kwargs['year'])

#def stddet(request,id):
	#std = get_object_or_404(students, id=id)
	
	#return render(request, 'Events/student.html',{'std': std})



def stdsearch(request):
	if request.method == 'GET':
		 search_query = request.GET.get('search_box', None)
		 evestudent= students.objects.filter(student_name=search_query)
	
	return render(request, 'Events/stdlist2.html',{'st':evestudent})	 


def register(request,id):
	if request.method=="POST":
		form = regi(request.POST)
		if form.is_valid():			
			#event_name=request.POST.get("name")
			event_obj=get_object_or_404(event,id=id)			
			if event_obj.no_of_seats>0:			
				#s_id = request.POST.get("clgId")
				#s_id = form.cleaned_data.get("clgId")
				#s_event = form.cleaned_data.get("name")
				#s_present = None
				#s_present = students.objects.filter(name=s_event)
				#s_present2 = students.objects.filter(clgId=s_id)
				#if s_present2 == None:
				event_obj.no_of_seats-=1

				#result = event_obj.objects.all().annotate(diff=F('total_seats')-F('no_of_seats'))
				#std = regi.cleaned_data[]
				event_obj.save()
				form.save()
				return HttpResponse("<h1>Seat booked successfully</h1>")
				#else:
				#return HttpResponse("<h1>student with this college Id already registered</h1>")
			else:
				return HttpResponse("<h1>No Vacancies</h1>")			
	else:
		form=regi()
	context={'form': form}
	return render(request,'Events/trialform.html',context)


def addevent(request):
	if request.method=="POST":
		form = add_event(request.POST)
		if form.is_valid():
			
				form.save()
				return HttpResponse("<h1>Event added successfully</h1>")
			
	else:
		form=add_event()
	context={'form': form}
	return render(request,'Events/addeventform.html',context)


def login(request):
	#user = User.objects.all()
	if request.method=="POST":

		
		key = request.POST.get('username')
		value = request.POST.get('password')
		#key1 = user.Uname
		if  key == 'admin':
			if value == 'pass':
				return redirect('adminpage')
			else:
				return HttpResponse("<h1>Incorrect password</h1>")	
		else:
			return HttpResponse("<h1>Incorrrect username</h1>")
		#form.save()	
	return render(request,'Events/login.html', {})