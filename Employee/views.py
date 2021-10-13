from django.shortcuts import render,HttpResponse
from Feedapp.models import FeedBackQuestions,Course,FeedBack



# util functions

def create_consolidated(feedbacks):
    a1_counts = [[n.A1 for n in feedbacks].count(i) for i in range(2,11)]
    a2_counts = [[n.A2 for n in feedbacks].count(i) for i in range(2,11)]
    a3_counts = [[n.A3 for n in feedbacks].count(i) for i in range(2,11)]
    a4_counts = [[n.A4 for n in feedbacks].count(i) for i in range(2,11)]
    a5_counts = [[n.A5 for n in feedbacks].count(i) for i in range(2,11)]
    a6_counts = [[n.A6 for n in feedbacks].count(i) for i in range(2,11)]
    a7_counts = [[n.A7 for n in feedbacks].count(i) for i in range(2,11)]
    a8_counts = [[n.A8 for n in feedbacks].count(i) for i in range(2,11)]
    a9_counts = [[n.A9 for n in feedbacks].count(i) for i in range(2,11)]
    a10_counts = [[n.A10 for n in feedbacks].count(i) for i in range(2,11)]
    a11_counts = [[n.A11 for n in feedbacks].count(i) for i in range(2,11)]
    a12_counts = [[n.A12 for n in feedbacks].count(i) for i in range(2,11)]
    a1_dic = {'c2_4':sum(a1_counts[:3]),'c5_6':sum(a1_counts[3:5]),'c7_8':sum(a1_counts[5:7]),'c9_10':sum(a1_counts[7:9])}
    a2_dic = {'c2_4':sum(a2_counts[:3]),'c5_6':sum(a2_counts[3:5]),'c7_8':sum(a2_counts[5:7]),'c9_10':sum(a2_counts[7:9])}
    a3_dic = {'c2_4':sum(a3_counts[:3]),'c5_6':sum(a3_counts[3:5]),'c7_8':sum(a3_counts[5:7]),'c9_10':sum(a3_counts[7:9])}
    a4_dic = {'c2_4':sum(a4_counts[:3]),'c5_6':sum(a4_counts[3:5]),'c7_8':sum(a4_counts[5:7]),'c9_10':sum(a4_counts[7:9])}
    a5_dic = {'c2_4':sum(a5_counts[:3]),'c5_6':sum(a5_counts[3:5]),'c7_8':sum(a5_counts[5:7]),'c9_10':sum(a5_counts[7:9])}
    a6_dic = {'c2_4':sum(a6_counts[:3]),'c5_6':sum(a6_counts[3:5]),'c7_8':sum(a6_counts[5:7]),'c9_10':sum(a6_counts[7:9])}
    a7_dic = {'c2_4':sum(a7_counts[:3]),'c5_6':sum(a7_counts[3:5]),'c7_8':sum(a7_counts[5:7]),'c9_10':sum(a7_counts[7:9])}
    a8_dic = {'c2_4':sum(a8_counts[:3]),'c5_6':sum(a8_counts[3:5]),'c7_8':sum(a8_counts[5:7]),'c9_10':sum(a8_counts[7:9])}
    a9_dic = {'c2_4':sum(a9_counts[:3]),'c5_6':sum(a9_counts[3:5]),'c7_8':sum(a9_counts[5:7]),'c9_10':sum(a9_counts[7:9])}
    a10_dic = {'c2_4':sum(a10_counts[:3]),'c5_6':sum(a10_counts[3:5]),'c7_8':sum(a10_counts[5:7]),'c9_10':sum(a10_counts[7:9])}
    a11_dic = {'c2_4':sum(a11_counts[:3]),'c5_6':sum(a11_counts[3:5]),'c7_8':sum(a11_counts[5:7]),'c9_10':sum(a11_counts[7:9])}
    a12_dic = {'c2_4':sum(a12_counts[:3]),'c5_6':sum(a12_counts[3:5]),'c7_8':sum(a12_counts[5:7]),'c9_10':sum(a12_counts[7:9])}
    return {"a1":list(a1_dic.values()),"a2":list(a2_dic.values()),"a3":list(a3_dic.values()),'a4':list(a4_dic.values()),'a5':list(a5_dic.values()),'a6':list(a6_dic.values()),
    'a7':list(a7_dic.values()),"a8":list(a8_dic.values()),'a9':list(a9_dic.values()),'a10':list(a10_dic.values()),'a11':list(a11_dic.values()),'a12':list(a12_dic.values())}
# Create your views here.
def home(request):
    return HttpResponse('this is employee home')

def ViewConsolidatedFeedback(request):
    # questions = FeedBackQuestions.objects.all()[0]
    faculty_questions =  FeedBackQuestions.objects.values_list("Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10","Q11","Q12")
    question_list = faculty_questions[0]
    q1_11         = question_list[:11]
    q12           = question_list[11]
    feedbacks = FeedBack.objects.filter(course_id='PGDTD-30',subject='Catia')
    feedback_con = list(create_consolidated(feedbacks).values())
    qna = dict.fromkeys(q1_11)
    for index,key in enumerate(qna):
        qna[key]=feedback_con[index]

    print(qna)
    return render(request,'feedbackConsolidated copy.html',{'Fac_qna':qna,'q12':q12,})