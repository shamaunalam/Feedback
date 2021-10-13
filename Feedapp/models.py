from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# from Employee.models import EmployeeProfile
# from Trainee.models import TraineeProfile
# Create your models here.

class Course(models.Model):

    course_id = models.CharField(max_length=50,primary_key=True)
    course_name = models.CharField(max_length=50,blank=False)
    faculty    = models.ForeignKey("Employee.EmployeeProfile", verbose_name=_("Faculty"), on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date   = models.DateField(blank=True)
    def __str__(self):
        return self.course_id

class FeedBackQuestions(models.Model):

    Q1 = models.TextField(max_length=100,blank =False)
    Q2 = models.TextField(max_length=100,blank=False)
    Q3 = models.TextField(max_length=100,blank=False)
    Q4 = models.TextField(max_length=100,blank=False)
    Q5 = models.TextField(max_length=100,blank=False)
    Q6 = models.TextField(max_length=100,blank=False)
    Q7 = models.TextField(max_length=100,blank=False)
    Q8 = models.TextField(max_length=100,blank=False)
    Q9 = models.TextField(max_length=100,blank=False)
    Q10 = models.TextField(max_length=100,blank=False)
    Q11 = models.TextField(max_length=100,blank=False)
    Q12 = models.TextField(max_length=100,blank=False)
    Q13 = models.TextField(max_length=100,blank=False,default="Safety")
    Q14 = models.TextField(max_length=100,blank=False,default="Training Admin Response")
    Q15 = models.TextField(max_length=100,blank=False,default="Cafeteria")
    Q16 = models.TextField(max_length=100,blank=False,default="Sanitation")
    Q17 = models.TextField(max_length=100,blank=False,default="Whether Course Duration is")
    Q18 = models.TextField(max_length=100,blank=False,default='Course To Be recommended')

    def __str__(self):
        return 'Feeback Questions Do not Add new'

class FeedBack(models.Model):

    class AmenitiesChoices(models.TextChoices):
        AM1 = "POOR",_("POOR")
        AM2 = "SATS",_("SATISFACTORY")
        AM3 = "GOOD" ,_("GOOD")
        AM4 = "EXCL",_("EXCELLENT")

    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    subject   = models.CharField(max_length=50,default='Others')
    A1        = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A2        = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A3        = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A4        = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A5        = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A6        = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A7        = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A8        = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A9        = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A10       = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A11       = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A12       = models.IntegerField(choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=0)
    A13       = models.CharField(max_length=4,choices=AmenitiesChoices.choices,default=AmenitiesChoices.AM3)
    A14       = models.CharField(max_length=4,choices=AmenitiesChoices.choices,default=AmenitiesChoices.AM3)
    A15       = models.CharField(max_length=4,choices=AmenitiesChoices.choices,default=AmenitiesChoices.AM3)
    A16       = models.CharField(max_length=4,choices=AmenitiesChoices.choices,default=AmenitiesChoices.AM3)
    A17       = models.CharField(max_length=2,choices=(("TS","Too Short"),("AD","Adequate"),("TL","Too Long")))
    A18       = models.CharField(max_length=2,choices=(("Y","Yes"),("N","No")))
    comments  = models.TextField(max_length=300,default="No Comments")
    def __str__(self):
        return "{} {}".format(self.user.first_name+' '+self.user.last_name,self.course_id)
    


