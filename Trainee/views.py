from django.shortcuts import render,redirect
from .models import CourseTaken,TraineeProfile
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.

@login_required(login_url='login')
@user_passes_test(lambda user:not user.is_staff,login_url='login')
def home(request):
        
    name = request.user.first_name+" "+request.user.last_name
    courses = CourseTaken.objects.filter(user=request.user)
    return render(request,'TraineeDash.html',{"name":name,"courses":courses})
