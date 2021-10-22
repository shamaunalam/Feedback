import os
from django.db import models
from django.contrib.auth.models import User
from Feedapp.models import Course,Department
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class EmployeeProfile(models.Model):
    class DesignationChoices(models.TextChoices):
        D1 = "GM",_("General Manager")
        D2 = "SM",_("Senior Manager")
        D3 = "MR",_("Manager")
        D4 = "SE",_("Senior Engineer")
        D5 = "ER",_("Engineer")
        D6 = "MC",_("Master Craftsman")
        D7 = "CO",_("Consultant")
        D8 = "GE",_("Graduate Engineer Trainee")
        D9 = "DE",_("Diploma Engineer Trainee")
        D10= "OJ",_("On Job Trainee")

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    department = models.ForeignKey(Department,to_field="department_name",on_delete=models.DO_NOTHING,default='OT')
    desg = models.TextField(_("Designation"),max_length=10,choices=DesignationChoices.choices,blank=True)
    qual = models.TextField(_("Qualification"),max_length=20,blank=True)
    photo = models.ImageField(upload_to='Employee_Photos',default='default_avatar.png')
    phone = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username+' '+'profile'

    def __getUser__(self):
        return self.user
