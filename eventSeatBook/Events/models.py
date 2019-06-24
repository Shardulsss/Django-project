from django.db import models
from django.db import models
import  datetime
class event(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    day = models.DateField(("Date"), default=datetime.date.today)
    no_of_seats = models.IntegerField()
    is_done = models.BooleanField(default=False)
    def __str__(self):
        return self.name +" " +self.place

        
class students(models.Model):
    student_name = models.CharField(max_length=50)
    Branch_Choices=(('INFT','INFT'), ('COMPS','COMPS'), ('CIVIL','CIVIL'), ('MECH','MECH'), ('INST','INST'))
    Branch = models.CharField(max_length=10,choices=Branch_Choices,default='aa')
    year_choices = (('FE','FE'), ('SE','SE'), ('TE','TE'), ('BE','BE')) 
    year = models.CharField(max_length=10,choices=year_choices,default='aa')
    clgId = models.CharField(max_length=10)
    name = models.ForeignKey(event, on_delete=models.CASCADE)
    Attendance = models.BooleanField(default=False)
    def __str__(self):
        return self.student_name +" " +self.Branch












class User(models.Model):
    Uname = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    def __str__(self):
        return self.Uname 