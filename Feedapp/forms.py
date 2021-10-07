from django.forms import ModelForm
from django.forms import Form
from django import forms
from .models import FeedBackQuestions,FeedBack
from django.utils.translation import gettext_lazy as _


class FeedBackForm(ModelForm):

    def __init__(self,*args,**kwargs):
       super(FeedBackForm, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

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
            'A1':forms.RadioSelect(attrs={'class': 'inline'}),
            'A2':forms.RadioSelect(attrs={'class': 'inline'}),
            'A3':forms.RadioSelect(attrs={'class': 'inline'}),
            'A4':forms.RadioSelect(attrs={'class': 'inline'}),
            'A5':forms.RadioSelect(attrs={'class': 'inline'}),
            'A6':forms.RadioSelect(attrs={'class': 'inline'}),
            'A7':forms.RadioSelect(attrs={'class': 'inline'}),
            'A8':forms.RadioSelect(attrs={'class': 'inline'}),
            'A9':forms.RadioSelect(attrs={'class': 'inline'}),
            'A10':forms.RadioSelect(attrs={'class': 'inline'}),
            'A11':forms.RadioSelect(attrs={'class': 'inline'}),
            'A12':forms.RadioSelect(attrs={'class': 'inline'}),
            }