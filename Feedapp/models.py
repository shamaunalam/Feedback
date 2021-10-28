from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# from Employee.models import EmployeeProfile
# from Trainee.models import TraineeProfile
# Create your models here.

class Department(models.Model):

    class DepartmentChoices(models.TextChoices):
        D1 = "PGDTD",_("Post Graduate Diploma in Tool Design")
        D2 = "MCC",_("Master Certificate Course In CAD/CAM")
        D3 = "PDTDM",_("Post Diploma In Tool and Die Making")
        D4 = "PDCC",_("Post Diploma in CAD/CAM")
        D5 = "CNC",_("Computer Numeric Control")
        D6 = "ITI",_("ITI")
        D7 = "DDUGKY",_("DDUGKY")
        D8 = "CIVIL",_("CIVIL")
        D9 = "DTDM",_("Diploma In Tool and Die Making")
        D10= "DIM",_("Diploma in Mechatronics")
        D11= "MCCAPC",_("MCCAPC")
        D12="ADMA",_("ADMA")
        D13="IoT",_("Internet Of Things")
        D14="PE",_("Power Electronics")
        D15="VLSI",_("Very Large Scale Integration")
        D16="OT",_("Others")

    department_name = models.TextField(max_length=20,choices=DepartmentChoices.choices,primary_key=True)
    incharge = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True)
    section = models.TextField(max_length=10,choices=(("CAD","CAD/CAM"),
    ("EB","Electronics Block"),("CV","Civil")),default="CAD")

    def __str__(self):
        return self.department_name
        



class Course(models.Model):

    course_id = models.CharField(max_length=50,primary_key=True)
    subject   = models.CharField(max_length=50,default='Others')
    course_details = models.CharField(max_length=500,blank=False)
    faculty    = models.ForeignKey("Employee.EmployeeProfile", verbose_name=_("Faculty"), on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date   = models.DateField(blank=True)
    start_time = models.TimeField(blank=True)
    end_time   = models.TimeField(blank=True)
    venue      = models.CharField(max_length=10,blank=True)
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

    class Meta:
        verbose_name_plural = 'Feedback Questions'

class FeedBack(models.Model):

    class AmenitiesChoices(models.TextChoices):
        AM1 = "POOR",_("POOR")
        AM2 = "SATS",_("SATISFACTORY")
        AM3 = "GOOD" ,_("GOOD")
        AM4 = "EXCL",_("EXCELLENT")

    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    A1        = models.IntegerField(_("How well the course was organised?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A2        = models.IntegerField(_("How confident do you feel about your grasp of this module content ?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A3        = models.IntegerField(_("How do you rate the learning environment during your training?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A4        = models.IntegerField(_("How satisfied you are by the training facility provided to you?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A5        = models.IntegerField(_("How was the quality of study material provided to you?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A6        = models.IntegerField(_("How effective do you find the faculty?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A7        = models.IntegerField(_("How satisfactory did you find their answers to your queries?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A8        = models.IntegerField(_("How thorough was their knowledge of course contents?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A9        = models.IntegerField(_("How inspiring was your association with the faculty?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A10       = models.IntegerField(_("How do you rate the assistance provided during your training?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A11       = models.IntegerField(_("How effective was the consultation provided?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A12       = models.IntegerField(_("How well were the stated objectives of the module achieved?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False)
    A13       = models.CharField(_("Safety"),max_length=4,choices=AmenitiesChoices.choices)
    A14       = models.CharField(_("Training Admin Response"),max_length=4,choices=AmenitiesChoices.choices)
    A15       = models.CharField(_("Cafeteria"),max_length=4,choices=AmenitiesChoices.choices)
    A16       = models.CharField(_("Sanitation"),max_length=4,choices=AmenitiesChoices.choices)
    A17       = models.CharField(_("Whether Course Duration is"),max_length=2,choices=(("TS","Too Short"),("AD","Adequate"),("TL","Too Long")))
    A18       = models.CharField(_("Course To Be recommended"),max_length=2,choices=(("Y","Yes"),("N","No")))
    comments  = models.TextField(_("Comments"),max_length=300,default="No Comments")
    def __str__(self):
        return "{} {}".format(self.user.first_name+' '+self.user.last_name,self.course_id)
    class Meta:
        verbose_name_plural = 'Feedbacks'
    

