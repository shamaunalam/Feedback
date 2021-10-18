from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# from Employee.models import EmployeeProfile
# from Trainee.models import TraineeProfile
# Create your models here.

class Course(models.Model):

    course_id = models.CharField(max_length=50,primary_key=True)
    subject   = models.CharField(max_length=50,default='Others')
    course_name = models.CharField(max_length=50,blank=False)
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
    A1        = models.IntegerField(_("How well the course was organised?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A2        = models.IntegerField(_("How confident do you feel about your grasp of this module content ?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A3        = models.IntegerField(_("How do you rate the learning environment during your training?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A4        = models.IntegerField(_("How satisfied you are by the training facility provided to you?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A5        = models.IntegerField(_("How was the quality of study material provided to you?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A6        = models.IntegerField(_("How effective do you find the faculty?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A7        = models.IntegerField(_("How satisfactory did you find their answers to your queries?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A8        = models.IntegerField(_("How thorough was their knowledge of course contents?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A9        = models.IntegerField(_("How inspiring was your association with the faculty?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A10       = models.IntegerField(_("How do you rate the assistance provided during your training?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A11       = models.IntegerField(_("How effective was the consultation provided?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A12       = models.IntegerField(_("How well were the stated objectives of the module achieved?"),choices=list(zip(range(2, 11), range(2, 11))),blank=False,default=None)
    A13       = models.CharField(_("Safety"),max_length=4,choices=AmenitiesChoices.choices,default=AmenitiesChoices.AM3)
    A14       = models.CharField(_("Training Admin Response"),max_length=4,choices=AmenitiesChoices.choices,default=AmenitiesChoices.AM3)
    A15       = models.CharField(_("Cafeteria"),max_length=4,choices=AmenitiesChoices.choices,default=AmenitiesChoices.AM3)
    A16       = models.CharField(_("Sanitation"),max_length=4,choices=AmenitiesChoices.choices,default=AmenitiesChoices.AM3)
    A17       = models.CharField(_("Whether Course Duration is"),max_length=2,choices=(("TS","Too Short"),("AD","Adequate"),("TL","Too Long")))
    A18       = models.CharField(_("Course To Be recommended"),max_length=2,choices=(("Y","Yes"),("N","No")))
    comments  = models.TextField(_("Comments"),max_length=300,default="No Comments")
    def __str__(self):
        return "{} {}".format(self.user.first_name+' '+self.user.last_name,self.course_id)
    class Meta:
        verbose_name_plural = 'Feedbacks'
    


