from django.db import models
from django.contrib.auth.models import User
from Feedapp.models import Course
# Create your models here.
class EmployeeProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username+' '+'profile'
