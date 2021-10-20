from django.contrib import admin
from .models import Course,FeedBackQuestions,FeedBack,Department
# Register your models here.
admin.site.register(Course)
admin.site.register(FeedBackQuestions)
admin.site.register(FeedBack)
admin.site.register(Department)