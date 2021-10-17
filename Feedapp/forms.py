from django.forms import ModelForm
from django import forms
from .models import FeedBackQuestions,FeedBack
from django.utils.translation import gettext_lazy as _


class FeedBackForm(ModelForm):

    def __init__(self,*args,**kwargs):
       super(FeedBackForm, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True
       self.fields['course_id'].widget.attrs['readonly']=True

    class Meta:
        questions = FeedBackQuestions.objects.all()[0]
        model = FeedBack
        fields = "__all__"
        labels = {
            'A1':_(questions.Q1),
            'A2':_(questions.Q2),
            'A3':_(questions.Q3),
            'A4':_(questions.Q4),
            'A5':_(questions.Q5),
            'A6':_(questions.Q6),
            'A7':_(questions.Q7),
            'A8':_(questions.Q8),
            'A9':_(questions.Q9),
            'A10':_(questions.Q10),
            'A11':_(questions.Q11),
            'A12':_(questions.Q12),
            'A13':_(questions.Q13),
            'A14':_(questions.Q14),
            'A15':_(questions.Q15),
            'A16':_(questions.Q16),
            'A17':_(questions.Q17),
            'A18':_(questions.Q18),
            }
        widgets={
            'course_id':forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.HiddenInput(attrs={'class':'form-control'}),
            'A1':forms.Select(attrs={'class':'form-control'}), 
            'A2':forms.Select(attrs={'class':'form-control'}),
            'A3':forms.Select(attrs={'class':'form-control'}),
            'A4':forms.Select(attrs={'class':'form-control'}),
            'A5':forms.Select(attrs={'class':'form-control'}),
            'A6':forms.Select(attrs={'class':'form-control'}),
            'A7':forms.Select(attrs={'class':'form-control'}),
            'A8':forms.Select(attrs={'class':'form-control'}),
            'A9':forms.Select(attrs={'class':'form-control'}),
            'A10':forms.Select(attrs={'class':'form-control'}),
            'A11':forms.Select(attrs={'class':'form-control'}),
            'A12':forms.Select(attrs={'class':'form-control'}),
            'A13':forms.Select(attrs={'class':'form-control'}),
            'A14':forms.Select(attrs={'class':'form-control'}),
            'A15':forms.Select(attrs={'class':'form-control'}),
            'A16':forms.Select(attrs={'class':'form-control'}),
            'A17':forms.Select(attrs={'class':'form-control'}),
            'A18':forms.Select(attrs={'class':'form-control'}),
            'comments' :forms.TextInput(attrs={'class':'form-control'})
            }