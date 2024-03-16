from urllib import request
from django.shortcuts import redirect, render
from django.http import JsonResponse
from calsy.models import  *
# Create your views here.
def calculator(request):
    
    return render(request, 'calculator.html')
a=''
b=''
c=''
def register_page(request):
    if  request.method == 'POST':
        name=request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        # a=name
        # b=email
        # c=password
        user_details.objects.create(name=name,email=email,password=password)
        return redirect('login')
    return render(request,'register.html')

def login_page(request):
    if  request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if user_details.objects.filter(email=email , password=password):
            return render(request,'form.html')
        else:
            return render(request,'register.html')
    return render(request,'login.html')

def homepage(request):

    return render(request,'homepage.html')
# def login(request):
#     if  request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         if  (email=='admin@gmail.com' and password=='123456'):
#             print('33333')
#             return render(request,"form.html")
        
#         else:
#             peinr('222222')
#             # data="error"
#             # return JsonResponse(data, safe=False)
#             return redirect('login/')
#     return render(request, "login.html")
    
def form(request):
    print("hai")
    if(request.method == "POST"):
        print("---------------")
        name= request.POST['name']
        dob= request.POST['DOB']

        AboutMe= request.POST['AboutMe']
        EmailId= request.POST['EmailId']
        Skills1= request.POST['Skills1']
        Skills2= request.POST['Skills2']
        Skills3= request.POST['Skills3']
        Skills4= request.POST['Skills4']
        Skills5= request.POST['Skills5']
        LanguagesKnown1= request.POST['LanguagesKnown1']
        LanguagesKnown2= request.POST['LanguagesKnown2']
        LanguagesKnown3= request.POST['LanguagesKnown3']
        sslc= request.POST['sslc']
        sslcyear= request.POST['sslcyear']
        sslcmark= request.POST['sslcmark']
        hsc= request.POST['hsc']
        hscyear= request.POST['hscyear']
        hscmark= request.POST['hscmark']
        degree= request.POST['Degree']
        # degreecourse= request.POST['degreecourse']
        CollegeName= request.POST['CollegeName']
        year= request.POST['year']
        cgpa= request.POST['cgpa']
        ProjectTitle1= request.POST['ProjectTitle1']
        ProjectTitle2= request.POST['ProjectTitle2']
        Duration1= request.POST['Duration1']
        Duration2= request.POST['Duration2']
        Description1= request.POST['Description1']
        Description2= request.POST['Description2']
        AchievementType1= request.POST['AchievementType1']
        AchievementType2= request.POST['AchievementType2']
        AchievementType3= request.POST['AchievementType3']
        
        datass={
           'name':name, 
           'dob':dob, 
           'aboutme':AboutMe, 
           'emailid':EmailId,
           'skills1':Skills1,
           'skills2':Skills2,
           'skills3':Skills3,
           'skills4':Skills4,
           'skills5':Skills5,
           'langknown1':LanguagesKnown1,
           'langknown2':LanguagesKnown2,
           'langknown3':LanguagesKnown3,
           'sslc':sslc,'sslcyear':sslcyear,'sslcmark':sslcmark,
           'hsc':hsc, 'hscmark': hscmark,"hscyear":hscyear ,
           'degree':degree,
        #    degreecourse,
           "CollegeName":CollegeName,
           "year":year,
           "cgpa":cgpa,
           'projecttitle1':ProjectTitle1,
           'projectduration1':Duration1,
           'projectdescription1':Description1,
           "ProjectTitle2":ProjectTitle2,
           "projectduration2":Duration2,
           "projectdescription2":Description2,
           "AchievementType1":AchievementType1,
           "AchievementType2":AchievementType2,
           "AchievementType3":AchievementType3,
            }
    
        return JsonResponse(datass, safe=False)

    return render(request, "form.html")