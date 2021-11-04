from Employee.models import EmployeeProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render,HttpResponse
from Feedapp.models import FeedBackQuestions,Course,FeedBack,Department
from Trainee.models import CourseTaken
from django.contrib.auth.models import User
import openpyxl


# util functions

def feedbackToStars(feedback):
    total_score = sum((feedback.A1,feedback.A2,feedback.A3,feedback.A4,feedback.A5,feedback.A6,feedback.A7,feedback.A8,feedback.A9,feedback.A10,feedback.A11))
    n_stars = (total_score//10)//2
    return n_stars


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
    a13_counts = [[n.A13 for n in feedbacks].count(i) for i in ["POOR","SATS","GOOD","EXCL"]]
    a14_counts = [[n.A14 for n in feedbacks].count(i) for i in ["POOR","SATS","GOOD","EXCL"]]
    a15_counts = [[n.A15 for n in feedbacks].count(i) for i in ["POOR","SATS","GOOD","EXCL"]]
    a16_counts = [[n.A16 for n in feedbacks].count(i) for i in ["POOR","SATS","GOOD","EXCL"]]

    a17_counts = [[n.A17 for n in feedbacks].count(i) for i in ["TS","AD","TL"]]
    a18_counts = [[n.A18 for n in feedbacks].count(i) for i in ["Y","N"]]

    zeroone = lambda x:1 if x==0 else x
    a1_dic = {'c2_4':sum(a1_counts[:3]),'t2_4':sum(a1_counts[:3])*3,'c5_6':sum(a1_counts[3:5]),'t5_6':sum(a1_counts[3:5])*5.5,'c7_8':sum(a1_counts[5:7]),'t7_8':sum(a1_counts[5:7])*7.5,'c9_10':sum(a1_counts[7:9]),'t9_10':sum(a1_counts[7:9])*9.5}
    a1_dic.update({"st":a1_dic['t2_4']+a1_dic['t5_6']+a1_dic['t7_8']+a1_dic['t9_10']})
    a1_dic.update({'avg':round(a1_dic['st']/zeroone(sum(a1_counts)),2)})

    a2_dic = {'c2_4':sum(a2_counts[:3]),'t2_4':sum(a2_counts[:3])*3,'c5_6':sum(a2_counts[3:5]),'t5_6':sum(a2_counts[3:5])*5.5,'c7_8':sum(a2_counts[5:7]),'t7_8':sum(a2_counts[5:7])*7.5,'c9_10':sum(a2_counts[7:9]),'t9_10':sum(a2_counts[7:9])*9.5}
    a2_dic.update({"st":a2_dic['t2_4']+a1_dic['t5_6']+a2_dic['t7_8']+a2_dic['t9_10']})
    a2_dic.update({'avg':round(a2_dic['st']/zeroone(sum(a2_counts)),2)})   
    
    a3_dic = {'c2_4':sum(a3_counts[:3]),'t2_4':sum(a3_counts[:3])*3,'c5_6':sum(a3_counts[3:5]),'t5_6':sum(a3_counts[3:5])*5.5,'c7_8':sum(a3_counts[5:7]),'t7_8':sum(a3_counts[5:7])*7.5,'c9_10':sum(a3_counts[7:9]),'t9_10':sum(a3_counts[7:9])*9.5}
    a3_dic.update({"st":a3_dic['t2_4']+a3_dic['t5_6']+a3_dic['t7_8']+a3_dic['t9_10']})
    a3_dic.update({'avg':round(a3_dic['st']/zeroone(sum(a3_counts)),2)})
    
    a4_dic = {'c2_4':sum(a4_counts[:3]),'t2_4':sum(a4_counts[:3])*3,'c5_6':sum(a4_counts[3:5]),'t5_6':sum(a4_counts[3:5])*5.5,'c7_8':sum(a4_counts[5:7]),'t7_8':sum(a4_counts[5:7])*7.5,'c9_10':sum(a4_counts[7:9]),'t9_10':sum(a4_counts[7:9])*9.5}
    a4_dic.update({"st":a4_dic['t2_4']+a4_dic['t5_6']+a4_dic['t7_8']+a4_dic['t9_10']})
    a4_dic.update({'avg':round(a4_dic['st']/zeroone(sum(a4_counts)),2)})   
    
    a5_dic = {'c2_4':sum(a5_counts[:3]),'t2_4':sum(a5_counts[:3])*3,'c5_6':sum(a5_counts[3:5]),'t5_6':sum(a5_counts[3:5])*5.5,'c7_8':sum(a5_counts[5:7]),'t7_8':sum(a5_counts[5:7])*7.5,'c9_10':sum(a5_counts[7:9]),'t9_10':sum(a5_counts[7:9])*9.5}
    a5_dic.update({"st":a5_dic['t2_4']+a5_dic['t5_6']+a5_dic['t7_8']+a5_dic['t9_10']})
    a5_dic.update({'avg':round(a5_dic['st']/zeroone(sum(a5_counts)),2)})
    
    a6_dic = {'c2_4':sum(a6_counts[:3]),'t2_4':sum(a6_counts[:3])*3,'c5_6':sum(a6_counts[3:5]),'t5_6':sum(a6_counts[3:5])*5.5,'c7_8':sum(a6_counts[5:7]),'t7_8':sum(a6_counts[5:7])*7.5,'c9_10':sum(a6_counts[7:9]),'t9_10':sum(a6_counts[7:9])*9.5}
    a6_dic.update({"st":a6_dic['t2_4']+a6_dic['t5_6']+a6_dic['t7_8']+a6_dic['t9_10']})
    a6_dic.update({'avg':round(a6_dic['st']/zeroone(sum(a6_counts)),2)})    
    
    a7_dic = {'c2_4':sum(a7_counts[:3]),'t2_4':sum(a7_counts[:3])*3,'c5_6':sum(a7_counts[3:5]),'t5_6':sum(a7_counts[3:5])*5.5,'c7_8':sum(a7_counts[5:7]),'t7_8':sum(a7_counts[5:7])*7.5,'c9_10':sum(a7_counts[7:9]),'t9_10':sum(a7_counts[7:9])*9.5}
    a7_dic.update({"st":a7_dic['t2_4']+a7_dic['t5_6']+a7_dic['t7_8']+a7_dic['t9_10']})
    a7_dic.update({'avg':round(a7_dic['st']/zeroone(sum(a7_counts)),2)})    
    
    a8_dic = {'c2_4':sum(a8_counts[:3]),'t2_4':sum(a8_counts[:3])*3,'c5_6':sum(a8_counts[3:5]),'t5_6':sum(a8_counts[3:5])*5.5,'c7_8':sum(a8_counts[5:7]),'t7_8':sum(a8_counts[5:7])*7.5,'c9_10':sum(a8_counts[7:9]),'t9_10':sum(a8_counts[7:9])*9.5}
    a8_dic.update({"st":a8_dic['t2_4']+a8_dic['t5_6']+a8_dic['t7_8']+a8_dic['t9_10']})
    a8_dic.update({'avg':round(a8_dic['st']/zeroone(sum(a8_counts)),2)})     
    
    
    a9_dic = {'c2_4':sum(a9_counts[:3]),'t2_4':sum(a9_counts[:3])*3,'c5_6':sum(a9_counts[3:5]),'t5_6':sum(a9_counts[3:5])*5.5,'c7_8':sum(a9_counts[5:7]),'t7_8':sum(a9_counts[5:7])*7.5,'c9_10':sum(a9_counts[7:9]),'t9_10':sum(a9_counts[7:9])*9.5}
    a9_dic.update({"st":a9_dic['t2_4']+a9_dic['t5_6']+a9_dic['t7_8']+a9_dic['t9_10']})
    a9_dic.update({'avg':round(a9_dic['st']/zeroone(sum(a9_counts)),2)})     
    
    a10_dic = {'c2_4':sum(a10_counts[:3]),'t2_4':sum(a10_counts[:3])*3,'c5_6':sum(a10_counts[3:5]),'t5_6':sum(a10_counts[3:5])*5.5,'c7_8':sum(a10_counts[5:7]),'t7_8':sum(a10_counts[5:7])*7.5,'c9_10':sum(a10_counts[7:9]),'t9_10':sum(a10_counts[7:9])*9.5}
    a10_dic.update({"st":a10_dic['t2_4']+a10_dic['t5_6']+a10_dic['t7_8']+a10_dic['t9_10']})
    a10_dic.update({'avg':round(a10_dic['st']/zeroone(sum(a10_counts)),2)})     
    
    a11_dic = {'c2_4':sum(a11_counts[:3]),'t2_4':sum(a11_counts[:3])*3,'c5_6':sum(a11_counts[3:5]),'t5_6':sum(a11_counts[3:5])*5.5,'c7_8':sum(a11_counts[5:7]),'t7_8':sum(a11_counts[5:7])*7.5,'c9_10':sum(a11_counts[7:9]),'t9_10':sum(a11_counts[7:9])*9.5}
    a11_dic.update({"st":a11_dic['t2_4']+a11_dic['t5_6']+a11_dic['t7_8']+a11_dic['t9_10']})
    a11_dic.update({'avg':round(a11_dic['st']/zeroone(sum(a11_counts)),2)})     
    
    a12_dic = {'c2_4':sum(a12_counts[:3]),'t2_4':sum(a12_counts[:3])*3,'c5_6':sum(a12_counts[3:5]),'t5_6':sum(a12_counts[3:5])*5.5,'c7_8':sum(a12_counts[5:7]),'t7_8':sum(a12_counts[5:7])*7.5,'c9_10':sum(a12_counts[7:9]),'t9_10':sum(a12_counts[7:9])*9.5}
    a12_dic.update({"st":a12_dic['t2_4']+a12_dic['t5_6']+a12_dic['t7_8']+a12_dic['t9_10']})
    a12_dic.update({'avg':round(a12_dic['st']/zeroone(sum(a12_counts)),2)})     

    a13_dic = {'cPoor':a13_counts[0],'cSats':a13_counts[1],'cGood':a13_counts[2],'cExcl':a13_counts[3]}
    a14_dic = {'cPoor':a14_counts[0],'cSats':a14_counts[1],'cGood':a14_counts[2],'cExcl':a14_counts[3]}
    a15_dic = {'cPoor':a15_counts[0],'cSats':a15_counts[1],'cGood':a15_counts[2],'cExcl':a15_counts[3]}
    a16_dic = {'cPoor':a16_counts[0],'cSats':a16_counts[1],'cGood':a16_counts[2],'cExcl':a16_counts[3]}

    a17_dic = {'cTS':a17_counts[0],'cAD':a17_counts[1],'cTL':a17_counts[2]}
    a18_dic = {'cY':a18_counts[0],'cN':a18_counts[1]}

    total_faculty_score = a1_dic['st']+a2_dic['st']+a3_dic['st']+a4_dic['st']+a5_dic['st']+a6_dic['st']+a7_dic['st']+a8_dic['st']+a9_dic['st']+a10_dic['st']+a11_dic['st']

    return {"a1":list(a1_dic.values()),"a2":list(a2_dic.values()),"a3":list(a3_dic.values()),'a4':list(a4_dic.values()),'a5':list(a5_dic.values()),'a6':list(a6_dic.values()),
    'a7':list(a7_dic.values()),"a8":list(a8_dic.values()),'a9':list(a9_dic.values()),'a10':list(a10_dic.values()),'a11':list(a11_dic.values()),'a12':list(a12_dic.values()),'a13':list(a13_dic.values()),'a14':list(a14_dic.values()),
    'a15':list(a15_dic.values()),'a16':list(a16_dic.values()),'a17':list(a17_dic.values()),'a18':list(a18_dic.values()),'total_faculty_score':total_faculty_score}
# Create your views here.

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff,login_url='oops')
def home(request):
        name = request.user.first_name.title()+" "+request.user.last_name.title()
        userpro = EmployeeProfile.objects.get(user=request.user)
        if userpro.desg in [EmployeeProfile.DesignationChoices.D1,EmployeeProfile.DesignationChoices.D2,EmployeeProfile.DesignationChoices.D3]:
            print(userpro.desg)
            all_courses = Course.objects.order_by("-start_date")
        elif userpro.department is not None:
            if userpro.department.incharge == request.user:
                # if user is incharge fetch all feedbacks of that department
                facpros = EmployeeProfile.objects.filter(department=userpro.department)
                all_courses = EmployeeProfile.objects.none()
                for fac in facpros:
                    courses = Course.objects.filter(faculty=fac)
                    all_courses = all_courses.union(courses)
                all_courses = all_courses.order_by('-start_date')
            else:
                all_courses = Course.objects.filter(faculty=userpro)
        else:
            all_courses = Course.objects.filter(faculty=userpro)
        return render(request,'EmployeeDash.html',{'name':name,'courses':all_courses,'userpro':userpro})
  

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff,login_url='oops')
def ViewConsolidatedFeedback(request,pk):
    course_id = pk
    faculty_questions =  FeedBackQuestions.objects.values_list("Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10","Q11","Q12","Q13","Q14","Q15","Q16","Q17","Q18")
    question_list = faculty_questions[0]
    q1_11         = question_list[:11]
    q12           = question_list[11]
    amnety_ques = question_list[12:16]
    other_ques  = question_list[16:18]
    feedbacks = FeedBack.objects.filter(course_id=course_id)
    if feedbacks.exists():
        name_of_course = " "+feedbacks[0].course_id.course_id
        name_of_faculty = feedbacks[0].course_id.faculty.user.first_name+" "+feedbacks[0].course_id.faculty.user.last_name
        start_date = feedbacks[0].course_id.start_date
        end_date = feedbacks[0].course_id.end_date
        timing = feedbacks[0].course_id.start_time.strftime("%I:%M %p")+' ~ '+feedbacks[0].course_id.end_time.strftime("%I:%M %p")
        duration = (start_date - end_date).days
        venue = feedbacks[0].course_id.venue
        number   = len(feedbacks)
        feedback_con = create_consolidated(feedbacks)
        total_faculty_score = feedback_con['total_faculty_score']
        avg_faculty_score = round((total_faculty_score/(number*110))*10,2)
        feedback_con = list(feedback_con.values())
        qna = dict.fromkeys(q1_11)
        for index,key in enumerate(qna):
            qna[key]=feedback_con[index]
            
        feedback_amnety = feedback_con[12:16]
        amnety_qna = dict.fromkeys(amnety_ques)
        for index,key in enumerate(amnety_qna):
            amnety_qna[key]=feedback_amnety[index]

        feedback_others = feedback_con[16:18]
        others_qna = dict.fromkeys(other_ques)
        for index,key in enumerate(others_qna):
            others_qna[key]=feedback_others[index]

        total_overall_score = total_faculty_score+feedback_con[11][8]
        avg_overall_score   = round((total_overall_score/(number*120))*10,2)

        n_stars_faculty = [1 for i in range(int(str(round(avg_faculty_score/2,1)).split('.')[0]))]
        if int(str(round(avg_faculty_score/2,1)).split('.')[1])>5:
            n_stars_faculty.append(1)
        elif int(str(round(avg_faculty_score/2,1)).split('.')[1])<=5 and int(str(round(avg_faculty_score/2,1)).split('.')[1])>0:
            n_stars_faculty.append(0.5)
        else:
            n_stars_faculty.append(0)

        if len(n_stars_faculty)>5:
            n_stars_faculty.pop()

        n_stars_center = [1 for i in range(int(str(round(feedback_con[11][9]/2,1)).split('.')[0]))]
        if int(str(round(feedback_con[11][9]/2,1)).split('.')[1])>5:
            n_stars_center.append(1)
        elif int(str(round(feedback_con[11][9]/2,1)).split('.')[1])<=5 and int(str(round(feedback_con[11][9]/2,1)).split('.')[1])>0:
            n_stars_center.append(0.5)
        else:
            n_stars_center.append(0)

        if len(n_stars_center)>5:
            n_stars_center.pop()

        n_stars_overall = [1 for i in range(int(str(round(avg_overall_score/2,1)).split('.')[0]))]
        if int(str(round(avg_overall_score/2,1)).split('.')[1])>5:
            n_stars_overall.append(1)
        elif int(str(round(avg_overall_score/2,1)).split('.')[1])<=5 and int(str(round(avg_overall_score/2,1)).split('.')[1])>0:
            n_stars_overall.append(0.5)
        else:
            n_stars_overall.append(0)

            if len(n_stars_overall)>5:
                n_stars_overall.pop()
            
        return render(request,'feedbackPDF.html',{"name_of_course":name_of_course,
        "name_of_faculty":name_of_faculty,'Fac_qna':qna,'q12':q12,'a12':feedback_con[11],"amnetyQna":amnety_qna,
        'others_qna':others_qna,'duration':duration,"start":start_date,"end":end_date,"timing":timing,'number':number,
        'total_faculty_score':total_faculty_score,'avg_faculty_score':avg_faculty_score,'total_overall_score':total_overall_score,
        'avg_overall_score':avg_overall_score,'venue':venue,'n_stars_faculty':n_stars_faculty,'n_stars_center':n_stars_center,
        'n_stars_overall':n_stars_overall})
    else:
        messages.error(request,'Feedback does not exist')
        return redirect('employee-home')

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff,login_url='oops')
def RegisterBulkStudents(request):
    """function to register bulk students"""
    name = request.user.first_name.title()+" "+request.user.last_name.title()
    userpro = EmployeeProfile.objects.get(user=request.user)
    if request.method=='POST':
        excl = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excl)
        worksheet = wb["Sheet1"]
        excel_data=[]
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        header = excel_data.pop(0)
        duplicates = 0
        for data in excel_data:
            try:
                user = User.objects.get(username=data[0])
                try:
                    course = Course.objects.get(course_id=data[1])
                    try:
                        coursetaken = CourseTaken.objects.get(user = user, course=course)
                        duplicates += 1
                    except CourseTaken.DoesNotExist:
                        coursetaken = CourseTaken.objects.create(user = user , course=Course.objects.get(course_id=data[1]))
                    finally:
                        coursetaken.save()
                except Course.DoesNotExist:
                    messages.error(request,"""{} Course Does not Exist Please ask admin to add the course!\n
                    Account for User {} could not be created""".format(data[1],data[0]))
                    continue
            except User.DoesNotExist:
                user = User.objects.create(username=data[0],first_name=data[2],last_name=data[3])
                user.set_password("P@55word")
                try:
                    course = Course.objects.get(course_id=data[1])
                except Course.DoesNotExist:
                    messages.error(request,"{} Course Does not Exist Please ask admin to add the course!".format(data[1]))
                    continue
                finally:
                    coursetaken = CourseTaken.objects.create(user = user , course=Course.objects.get(course_id=data[1]))
                    user.save()
                    coursetaken.save()
        if duplicates>0:
            messages.error(request,'{} users already registered for course'.format(duplicates))
        else:
            messages.success(request,"Trainees Successfully Registered!")
        return render(request,'bulk_test.html',{"name":name,"excel_data":excel_data,"userpro":userpro})
        
    else:
        return render(request,'bulk_test.html',{"name":name,"userpro":userpro})

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff,login_url='oops')
def eprofile(request,pk):
   name = request.user.first_name.title()+" "+request.user.last_name.title()
   if request.user.username==pk:
       try:
           userpro=EmployeeProfile.objects.get(user=request.user)
           pro = userpro
           courses_taken = Course.objects.filter(faculty=userpro)
           if courses_taken.filter(faculty=userpro).exists():
               stars=list()
               for course in courses_taken:
                   feedbacks = FeedBack.objects.filter(course_id=course)
                   for feedback in feedbacks:
                       stars.append(feedbackToStars(feedback))
               count_stars = [stars.count(5),stars.count(4),stars.count(3),stars.count(2),stars.count(1),stars.count(0)]
               total_stars = sum(count_stars)
               if total_stars!=0:
                    avg = round(sum(stars)/total_stars,1)
                    star_percent = [int((i/total_stars)*100) for i in count_stars]
               else:
                    avg = 0
                    star_percent = [0 for i in count_stars]
               context = {"count_stars":count_stars,'total_stars':total_stars,'star_percent':star_percent,
               'avg':avg,'flag':[1 for i in range(int(avg))],'pro':pro,'username':request.user.username.title(),'userpro':userpro,"name":name}
               return render(request,'EmployeeProfile.html',context)
           else:
               context = {"count_stars":[0,0,0,0,0],'total_stars':0,'star_percent':[0,0,0,0,0],
               'avg':0,'flag':[1 for i in range(int(0))],'pro':pro,'username':request.user.username.title(),'userpro':userpro,
               "name":name}
               return render(request,'EmployeeProfile.html',context)
       except EmployeeProfile.DoesNotExist:
           messages.error(request,'profile does not exist')
           return redirect('employee-home')
   else:
       userpro = EmployeeProfile.objects.get(user=request.user)
       if (userpro.desg in [EmployeeProfile.DesignationChoices.D1,EmployeeProfile.DesignationChoices.D2,EmployeeProfile.DesignationChoices.D3]) or userpro.department.incharge==request.user:
            try:
                pro = EmployeeProfile.objects.get(user=User.objects.get(username=pk))
                if (userpro.desg in [EmployeeProfile.DesignationChoices.D1,EmployeeProfile.DesignationChoices.D2,EmployeeProfile.DesignationChoices.D3]) or pro.department.incharge==request.user:
                    courses_taken = Course.objects.filter(faculty=pro)
                    if courses_taken.filter(faculty=pro).exists():
                        stars=list()
                        for course in courses_taken:
                            feedbacks = FeedBack.objects.filter(course_id=course)
                            for feedback in feedbacks:
                                stars.append(feedbackToStars(feedback))
                        count_stars = [stars.count(5),stars.count(4),stars.count(3),stars.count(2),stars.count(1),stars.count(0)]
                        total_stars = sum(count_stars)
                        if total_stars!=0:
                                avg = round(sum(stars)/total_stars,1)
                                star_percent = [int((i/total_stars)*100) for i in count_stars]
                        else:
                                avg = 0
                                star_percent = [0 for i in count_stars]
                        context = {"count_stars":count_stars,'total_stars':total_stars,'star_percent':star_percent,
                        'avg':avg,'flag':[1 for i in range(int(avg))],'pro':pro,'username':request.user.username.title(),'userpro':userpro,
                        "name":name}
                        return render(request,'EmployeeProfile.html',context)
                    else:
                        context = {"count_stars":[0,0,0,0,0],'total_stars':0,'star_percent':[0,0,0,0,0],
                        'avg':0,'flag':[1 for i in range(int(0))],'pro':pro,'username':request.user.username.title(),'userpro':userpro,
                        "name":name}
                        return render(request,'EmployeeProfile.html',context)
                else:
                    messages.error(request,'Access Denied')
                    return redirect('employee-home')                   
            except User.DoesNotExist:
                messages.error(request,'profile for {} does not exist'.format(pk))
                return redirect('employee-home')
       else:
           messages.error(request,'Access Denied')
           return redirect('employee-home')

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff,login_url='oops')
def search(request):
    if request.method=='POST':
        pk = request.POST['pk']
        try:
            emp= EmployeeProfile.objects.get(user=User.objects.get(username=pk))
            empId = emp.user.username
            return redirect('employee-profile',empId)
        except User.DoesNotExist:
            messages.error(request,'user does not exist')
            return redirect('employee-home')
    else:
        messages.error(request,'Nothing to search')
        redirect('employee-home')
