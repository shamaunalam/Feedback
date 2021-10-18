from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        return redirect('submitfeedback',pk)
    else:
        return render(request,'TraineeDash.html')