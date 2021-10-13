from django.shortcuts import redirect, render,HttpResponse
from .forms import FeedBackForm
from Trainee.models import TraineeProfile,CourseTaken

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def Login(request):
    if request.method=='POST':
        username = request.POST['uname']
        _password = request.POST['psw']
        user = authenticate(username=username,password=_password)
        if user is not None:
            login(request,user)
            return redirect('submitfeedback')
    else:

        return render(request,'login.html')


def getFeedback(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = FeedBackForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Thanks for providing your valuable feedback!')
        if not request.user.is_staff:
            coursetaken = CourseTaken.objects.filter(user=request.user,course='PGDTD-30')[0]
            try:
                name = request.user.first_name+' '+request.user.last_name
            except:
                name = request.user.username
            
            form = FeedBackForm(initial={'user':request.user,'course_id':coursetaken.course})
            
            return render(request,'basic.html',{'name':name,'form':form})
        
        else:
            form = FeedBackForm(initial={'user':request.user,'course_id':'Others'})

            return render(request,'basic.html',{'form':form})

