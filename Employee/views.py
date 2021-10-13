from django.shortcuts import render,HttpResponse
from Feedapp.models import FeedBackQuestions,Course,FeedBack
from Trainee.models import CourseTaken
from django.contrib.auth.models import User
import openpyxl


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
    zeroone = lambda x:1 if x==0 else x
    a1_dic = {'c2_4':sum(a1_counts[:3]),'t2_4':round((a1_counts[0]*2+a1_counts[1]*3+a1_counts[2]*4)/zeroone((a1_counts[0]+a1_counts[1]+a1_counts[2])),1),'c5_6':sum(a1_counts[3:5]),'t5_6':round((a1_counts[3]*5+a1_counts[4]*6)/zeroone((a1_counts[3]+a1_counts[4])),1),'c7_8':sum(a1_counts[5:7]),'t7_8':round((a1_counts[5]*7+a1_counts[6]*7)/zeroone((a1_counts[5]+a1_counts[6])),2),'c9_10':sum(a1_counts[7:9]),'t9_10':round((a1_counts[7]*9+a1_counts[8]*10)/zeroone((a1_counts[7]+a1_counts[8])),1)}
    a2_dic = {'c2_4':sum(a2_counts[:3]),'t2_4':round((a2_counts[0]*2+a2_counts[1]*3+a2_counts[2]*4)/zeroone((a2_counts[0]+a2_counts[1]+a2_counts[2])),1),'c5_6':sum(a2_counts[3:5]),'t5_6':round((a2_counts[3]*5+a2_counts[4]*6)/zeroone((a2_counts[3]+a2_counts[4])),1),'c7_8':sum(a2_counts[5:7]),'t7_8':round((a2_counts[5]*7+a2_counts[6]*7)/zeroone((a2_counts[5]+a2_counts[6])),2),'c9_10':sum(a2_counts[7:9]),'t9_10':round((a2_counts[7]*9+a2_counts[8]*10)/zeroone((a2_counts[7]+a2_counts[8])),1)}
    a3_dic = {'c2_4':sum(a3_counts[:3]),'t2_4':round((a3_counts[0]*2+a3_counts[1]*3+a3_counts[2]*4)/zeroone((a3_counts[0]+a3_counts[1]+a3_counts[2])),1),'c5_6':sum(a3_counts[3:5]),'t5_6':round((a3_counts[3]*5+a3_counts[4]*6)/zeroone((a3_counts[3]+a3_counts[4])),1),'c7_8':sum(a3_counts[5:7]),'t7_8':round((a3_counts[5]*7+a3_counts[6]*7)/zeroone((a3_counts[5]+a3_counts[6])),2),'c9_10':sum(a3_counts[7:9]),'t9_10':round((a3_counts[7]*9+a3_counts[8]*10)/zeroone((a3_counts[7]+a3_counts[8])),1)}
    a4_dic = {'c2_4':sum(a4_counts[:3]),'t2_4':round((a4_counts[0]*2+a4_counts[1]*3+a4_counts[2]*4)/zeroone((a4_counts[0]+a4_counts[1]+a4_counts[2])),1),'c5_6':sum(a4_counts[3:5]),'t5_6':round((a4_counts[3]*5+a4_counts[4]*6)/zeroone((a4_counts[3]+a4_counts[4])),1),'c7_8':sum(a4_counts[5:7]),'t7_8':round((a4_counts[5]*7+a4_counts[6]*7)/zeroone((a4_counts[5]+a4_counts[6])),2),'c9_10':sum(a4_counts[7:9]),'t9_10':round((a4_counts[7]*9+a4_counts[8]*10)/zeroone((a4_counts[7]+a4_counts[8])),1)}
    a5_dic = {'c2_4':sum(a5_counts[:3]),'t2_4':round((a5_counts[0]*2+a5_counts[1]*3+a5_counts[2]*4)/zeroone((a5_counts[0]+a5_counts[1]+a5_counts[2])),1),'c5_6':sum(a5_counts[3:5]),'t5_6':round((a5_counts[3]*5+a5_counts[4]*6)/zeroone((a5_counts[3]+a5_counts[4])),1),'c7_8':sum(a5_counts[5:7]),'t7_8':round((a5_counts[5]*7+a5_counts[6]*7)/zeroone((a5_counts[5]+a5_counts[6])),2),'c9_10':sum(a5_counts[7:9]),'t9_10':round((a5_counts[7]*9+a5_counts[8]*10)/zeroone((a5_counts[7]+a5_counts[8])),1)}
    a6_dic = {'c2_4':sum(a6_counts[:3]),'t2_4':round((a6_counts[0]*2+a6_counts[1]*3+a6_counts[2]*4)/zeroone((a6_counts[0]+a6_counts[1]+a6_counts[2])),1),'c5_6':sum(a6_counts[3:5]),'t5_6':round((a6_counts[3]*5+a6_counts[4]*6)/zeroone((a6_counts[3]+a6_counts[4])),1),'c7_8':sum(a6_counts[5:7]),'t7_8':round((a6_counts[5]*7+a6_counts[6]*7)/zeroone((a6_counts[5]+a6_counts[6])),2),'c9_10':sum(a6_counts[7:9]),'t9_10':round((a6_counts[7]*9+a6_counts[8]*10)/zeroone((a6_counts[7]+a6_counts[8])),1)}
    a7_dic = {'c2_4':sum(a7_counts[:3]),'t2_4':round((a7_counts[0]*2+a7_counts[1]*3+a7_counts[2]*4)/zeroone((a7_counts[0]+a7_counts[1]+a7_counts[2])),1),'c5_6':sum(a7_counts[3:5]),'t5_6':round((a7_counts[3]*5+a7_counts[4]*6)/zeroone((a7_counts[3]+a7_counts[4])),1),'c7_8':sum(a7_counts[5:7]),'t7_8':round((a7_counts[5]*7+a7_counts[6]*7)/zeroone((a7_counts[5]+a7_counts[6])),2),'c9_10':sum(a7_counts[7:9]),'t9_10':round((a7_counts[7]*9+a7_counts[8]*10)/zeroone((a7_counts[7]+a7_counts[8])),1)}
    a8_dic = {'c2_4':sum(a8_counts[:3]),'t2_4':round((a8_counts[0]*2+a8_counts[1]*3+a8_counts[2]*4)/zeroone((a8_counts[0]+a8_counts[1]+a8_counts[2])),1),'c5_6':sum(a8_counts[3:5]),'t5_6':round((a8_counts[3]*5+a8_counts[4]*6)/zeroone((a8_counts[3]+a8_counts[4])),1),'c7_8':sum(a8_counts[5:7]),'t7_8':round((a8_counts[5]*7+a8_counts[6]*7)/zeroone((a8_counts[5]+a8_counts[6])),2),'c9_10':sum(a8_counts[7:9]),'t9_10':round((a8_counts[7]*9+a8_counts[8]*10)/zeroone((a8_counts[7]+a8_counts[8])),1)}
    a9_dic = {'c2_4':sum(a9_counts[:3]),'t2_4':round((a9_counts[0]*2+a9_counts[1]*3+a9_counts[2]*4)/zeroone((a9_counts[0]+a9_counts[1]+a9_counts[2])),1),'c5_6':sum(a9_counts[3:5]),'t5_6':round((a9_counts[3]*5+a9_counts[4]*6)/zeroone((a9_counts[3]+a9_counts[4])),1),'c7_8':sum(a9_counts[5:7]),'t7_8':round((a9_counts[5]*7+a9_counts[6]*7)/zeroone((a9_counts[5]+a9_counts[6])),2),'c9_10':sum(a9_counts[7:9]),'t9_10':round((a9_counts[7]*9+a9_counts[8]*10)/zeroone((a9_counts[7]+a9_counts[8])),1)}
    a10_dic = {'c2_4':sum(a10_counts[:3]),'t2_4':round((a10_counts[0]*2+a10_counts[1]*3+a10_counts[2]*4)/zeroone((a10_counts[0]+a10_counts[1]+a10_counts[2])),1),'c5_6':sum(a10_counts[3:5]),'t5_6':round((a10_counts[3]*5+a10_counts[4]*6)/zeroone((a10_counts[3]+a10_counts[4])),1),'c7_8':sum(a10_counts[5:7]),'t7_8':round((a10_counts[5]*7+a10_counts[6]*7)/zeroone((a10_counts[5]+a10_counts[6])),1),'c9_10':sum(a10_counts[7:9]),'t9_10':round((a10_counts[7]*9+a10_counts[8]*10)/zeroone((a10_counts[7]+a10_counts[8])),1)}
    a11_dic = {'c2_4':sum(a11_counts[:3]),'t2_4':round((a11_counts[0]*2+a11_counts[1]*3+a11_counts[2]*4)/zeroone((a11_counts[0]+a11_counts[1]+a11_counts[2])),1),'c5_6':sum(a11_counts[3:5]),'t5_6':round((a11_counts[3]*5+a11_counts[4]*6)/zeroone((a11_counts[3]+a11_counts[4])),1),'c7_8':sum(a11_counts[5:7]),'t7_8':round((a11_counts[5]*7+a11_counts[6]*7)/zeroone((a11_counts[5]+a11_counts[6])),1),'c9_10':sum(a11_counts[7:9]),'t9_10':round((a11_counts[7]*9+a11_counts[8]*10)/zeroone((a11_counts[7]+a11_counts[8])),1)}
    a12_dic = {'c2_4':sum(a12_counts[:3]),'t2_4':round((a12_counts[0]*2+a12_counts[1]*3+a12_counts[2]*4)/zeroone((a12_counts[0]+a12_counts[1]+a12_counts[2])),1),'c5_6':sum(a12_counts[3:5]),'t5_6':round((a12_counts[3]*5+a12_counts[4]*6)/zeroone((a12_counts[3]+a12_counts[4])),1),'c7_8':sum(a12_counts[5:7]),'t7_8':round((a12_counts[5]*7+a12_counts[6]*7)/zeroone((a12_counts[5]+a12_counts[6])),1),'c9_10':sum(a12_counts[7:9]),'t9_10':round((a12_counts[7]*9+a12_counts[8]*10)/zeroone((a12_counts[7]+a12_counts[8])),1)}
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
    return render(request,'feedbackConsolidated copy.html',{'Fac_qna':qna,'q12':q12,'a12':feedback_con[11]})

def RegisterBulkStudents(request):

    if request.method=='POST':
        excl = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excl)
        sheets = wb.sheetnames
        worksheet = wb["Sheet1"]
        excel_data=[]
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
                print(cell.value)
            excel_data.append(row_data)
        header = excel_data.pop(0)
        print(header)
        print(excel_data)
        for data in excel_data:
            user = User.objects.create(username=data[0],first_name=data[2],last_name=data[-1])
            coursetaken = CourseTaken.objects.create(user = user , course=Course.objects.get(course_id=data[1]))
            user.set_password("p@55word")
            user.save()
            coursetaken.save()

        return render(request,'bulk_test.html',{"excel_data":excel_data})
    else:
        return render(request,'bulk_test.html',{})