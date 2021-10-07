from django.db import models
from django.contrib.auth.models import User
from Feedapp.models import Course
# Create your models here.
class TraineeProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=False,default='Others')
    date_admitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username+' '+'profile'