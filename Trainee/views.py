from django.shortcuts import render,redirect
from .models import CourseTaken,TraineeProfile
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if not request.user.is_staff:
            if request.method == 'POST':
                pk = request.POST['pk']
                return redirect('submitfeedback',pk)
            else:      
                name = request.user.first_name+" "+request.user.last_name
                courses = CourseTaken.objects.filter(user=request.user)
                return render(request,'TraineeDash.html',{"name":name,"courses":courses})
        else:
            return render(request,'restricted_access.htmlS')
    else:
        return redirect('login')       