from django.shortcuts import render,HttpResponse
from .forms import FeedBackForm
from Trainee.models import TraineeProfile
# Create your views here.
def Login(request):

    return HttpResponse('this is login for all')


def getFeedback(request):
    if request.user.is_authenticated:

        if not request.user.is_staff:
            pro = TraineeProfile.objects.get(user=request.user)

            form = FeedBackForm(initial={'user':request.user,'course_id':pro.course.course_id})

            return render(request,'feedbackform.html',{'form':form})
        
        else:
            form = FeedBackForm(initial={'user':request.user,'course_id':'Others'})

            return render(request,'index.html',{'form':form})