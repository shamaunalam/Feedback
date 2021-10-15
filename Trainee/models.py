from django.db import models
from django.contrib.auth.models import User
from Feedapp.models import Course
# Create your models here.
class TraineeProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    date_admitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username+' '+'profile'


class CourseTaken(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,default='Others')
    def __str__(self):
        return self.user.username+' '+self.course.course_id
    class Meta:
        verbose_name_plural = 'Taken Courses by Trainees'