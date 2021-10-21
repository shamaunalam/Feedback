from django.shortcuts import redirect, render,HttpResponse
from .forms import FeedBackForm
from Trainee.models import TraineeProfile,CourseTaken
from .models import FeedBack


from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
# Create your views here.

def oops(request):
    return render(request,'restricted_access.html')

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
                    return redirect('trainee-home')
            else:
                return redirect('login')
        else:

            return render(request,'login.html')
    else:
        if request.user.is_staff:
            return redirect('employee-home')
        else:
             return redirect('trainee-home')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

@login_required(login_url='login')
@user_passes_test(lambda user:not user.is_staff,login_url='login')
def getFeedback(request,pk):
    if request.method=='POST':
        form = FeedBackForm(request.POST)
            # print(cleaned_data)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            try:
                feedback = FeedBack.objects.get(user=cleaned_data['user'],course_id = cleaned_data['course_id'])
                messages.error(request, 'Feedback for course {} already Submitted!'.format(cleaned_data['course_id']))
            except FeedBack.DoesNotExist:
                form.save()
                messages.success(request, 'Thanks for providing your valuable feedback!')
            return redirect('submitfeedback',pk)
        else:
            messages.error(request, 'An Error occured while submitting the form')
            return redirect('submitfeedback',pk)
    else:
        coursetaken = CourseTaken.objects.filter(user=request.user,course=pk)[0]
        name = request.user.first_name+' '+request.user.last_name
        if name==' ':
            name = request.user.username
        form = FeedBackForm(initial={'user':request.user,'course_id':coursetaken.course})
                
        return render(request,'feedbackform.html',{'name':name,'form':form,'course_id':coursetaken.course,'pk':pk})

