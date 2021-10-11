from django.shortcuts import redirect, render,HttpResponse
from .forms import FeedBackForm
from Trainee.models import TraineeProfile

from django.contrib.auth import authenticate,login,logout
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

        if not request.user.is_staff:
            pro = TraineeProfile.objects.get(user=request.user)
            try:
                name = request.user.first_name+' '+request.user.last_name
            except:
                name = request.user.username
            
            form = FeedBackForm(initial={'user':request.user,'course_id':pro.course.course_id})
            print(name)
            return render(request,'basic.html',{'name':name,'form':form})
        
        else:
            form = FeedBackForm(initial={'user':request.user,'course_id':'Others'})

            return render(request,'basic.html',{'form':form})