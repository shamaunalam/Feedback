from django.shortcuts import redirect, render,HttpResponse
from .forms import FeedBackForm
from Trainee.models import TraineeProfile,CourseTaken

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def Login(request):
    if request.user.is_anonymous:
        if request.method=='POST':
            username = request.POST['username']
            _password = request.POST['password']
            user = authenticate(username=username,password=_password)
            if user is not None:
                login(request,user)
                if user.is_staff:
                    return redirect('employee-home')
                else:
                    return redirect('submitfeedback')
            else:
                return redirect('login')
        else:

            return render(request,'login.html')
    else:
        if request.user.is_staff:
            return redirect('employee-home')
        else:
             return redirect('submitfeedback')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

def getFeedback(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = FeedBackForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Thanks for providing your valuable feedback!')
        if not request.user.is_staff:
            coursetaken = CourseTaken.objects.filter(user=request.user,course='PGDTD-30 AIML')[0]
            try:
                name = request.user.first_name+' '+request.user.last_name
            except:
                name = request.user.username
            
            form = FeedBackForm(initial={'user':request.user,'course_id':coursetaken.course})
            
            return render(request,'basic.html',{'name':name,'form':form})
        
        else:
            form = FeedBackForm(initial={'user':request.user,'course_id':'Others'})

            return render(request,'basic.html',{'form':form})

