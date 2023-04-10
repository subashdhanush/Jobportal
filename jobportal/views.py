from ast import Return
from audioop import reverse
from datetime import date
import email
from email.message import EmailMessage
from itertools import count
from operator import add
import re
from sys import flags
from unicodedata import category
from urllib import request
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.core.mail import send_mail,BadHeaderError
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .models import EmployerContact, EmployeeDetails, EmployeeProfile, JobsekerProfile, Payment_Details, PostedJob,AppliedJobs,IdInformations, SavedJobs,CandidateSavedJobs,CandidateSaved,ContactDetail,Skills
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponse
import json
from django.http import JsonResponse
import smtplib
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponseRedirect
from paypal.standard.forms import PayPalPaymentsForm
from uuid import uuid4
from django.shortcuts import get_object_or_404
# from hitcount.views import HitCountDetailView
# from .models import Order
# from paypal.standard.ipn.signals import valid_ipn_received
# from django.dispatch import receiver

# from paypal.standard.forms import PayPalPaymentsForm
# from paypalcheckoutsdk.orders import OrdersGetRequest
# from .paypal import PayPalClient
from django.db.models import F


emailFrom = [settings.EMAIL_HOST_USER]




User = get_user_model()

# Create your views here.

# def empbase(request):
#     return render(request,'empbase.html')

def alertjobs(request):
    if request.user.is_authenticated:
     return render(request,'alertjobs.html')
    else:
        return render(request,'employeelogin.html') 


def candidatedappliedjobs(request):
  if request.user.is_authenticated:  
    email=request.user.email
    applylist=AppliedJobs.objects.filter(email=email,deleteflag='0')
    print(applylist)
    return render(request,'candidatedappliedjobs.html',{"listapply":applylist})
  else:
     return render(request,'candidatelogin.html')  


def candidatedresume(request):
 if request.user.is_authenticated:
    username=request.user.username
    email=request.user.email
    id=IdInformations.objects.get(username=username,email=email)
    # id=IdInformations.objects.get(username=username,email=email)
    # id=IdInformations.objects.get(email=email)
    userid=id.userid
    profileseeker=JobsekerProfile.objects.filter(fullname=username,userid=userid).exists()
    print("CANDIDATE RESUME",profileseeker)
    if request.method =='GET':
        username=request.user.username
        email=request.user.email
        id=IdInformations.objects.get(username=username,email=email)
        userid=id.userid
        # userid=request.user.userid
        print("jobsekker",username)
        print("userid",userid)
        profileseeker=JobsekerProfile.objects.filter(fullname=username,userid=userid).exists()
        if JobsekerProfile.objects.filter(fullname=username,userid=userid).exists():
         sekerlist=JobsekerProfile.objects.filter(fullname=username,userid=userid)
         return render(request,'candidatefilledform.html',{"sekerlist":sekerlist})
        else:
            print("INSIDE ELSE PART OF PROFILESEEEKER",profileseeker)
            return render(request,'candidatedresume.html',{"profileseeker":profileseeker})
    else:
        fullname=request.POST.get('fullname',False)
        qualification=request.POST.get('qualification',False)
        # resume=request.POST.get('resume',False)
        resume=request.FILES['resume']
        jobcategory=request.POST.get('jobcategory',False)
        jobtype=request.POST.get('jobtype',False)
        singaporean=request.POST.get('singaporean',False)
        salaryfrom=request.POST.get('salaryfrom',False)
        # skills=request.POST.getlist('skills[]',False)
        experience=request.POST.get('experience',False)
        contactnumber=request.POST.get('contactnumber',False)
        email=request.POST.get('email',False)
        address=request.POST.get('address',False)
        currentjob=request.POST.get('currentjob',False)
        userid=userid
        date=User.objects.get(username=username,email=email) 
        joined=date.date_joined
        candidateprofile=JobsekerProfile.objects.create(fullname=fullname,Qualification=qualification,fileupload=resume,jobcategory=jobcategory,jobtype=jobtype,singaporean=singaporean,salaryfrom=salaryfrom,experience=experience,contactnumber=contactnumber,email=email,address=address,userid=userid,currentjob=currentjob,datejoined=joined)
        candidateprofile.save()
        return redirect("/candidatedresume/")
    # return render(request,'candidatedresume.html',{"profileseeker":profileseeker})
    # return render(request,'candidatefilledform.html',{"profileseeker":profileseeker})
 else:
      return render(request,'candidatelogin.html')


def candidateddashboard(request):
  if request.user.is_authenticated:
    jobsearch=PostedJob.objects.all().order_by('id').reverse()
    username=request.user.username
    email=request.user.email
    ids=IdInformations.objects.filter(username=username,email=email)
    print(ids)
    count=AppliedJobs.objects.filter(email=email,flag='1',deleteflag='0').count()
    #  return render(request,'jobsekersearch.html',{"jobsearch":jobsearch})  
    return render(request,'candidateddashboard.html',{"jobsearch":jobsearch,"count":count})
  else:
    return render(request,'candidatelogin.html')  

def candidatedsavedjobs(request):
    if request.user.is_authenticated:
     username=request.user.username
     email=request.user.email
     ids=IdInformations.objects.get(username=username,email=email)
     userid=ids.userid
     list=CandidateSaved.objects.filter(username=username,userid=userid)
     print("listoutt",list)
     return render(request,'candidatedsavedjobs.html',{"list":list})
    else:
     return render(request,'candidatelogin.html')   

def index(request):
      if request.method=='POST':  
        query=request.GET.get('jobtitle','')
        if len(query)>0:
         jobsearch=PostedJob.objects.all().filter(Q(jobtitle__iexact=query) | Q(jobtitle__icontains=query) |Q(jobtitle__startswith=query)).distinct('jobtitle')
         print("queryyy",jobsearch)
         return render(request,'jobsearch.html',{"jobsearch":jobsearch})
        else:
         listofjob=PostedJob.objects.all().order_by('id').reverse()[:7]
         return render(request,'index.html',{"listofjob":listofjob})
        jobsearch=PostedJob.objects.filter(jobtitle__icontains=jobtitle)
        print("HEREEEEEEE IS THEEEEE",jobsearch)
        return render(request,'jobsearch.html',{"jobsearch":jobsearch})     
        # return redirect('jobsekersearch',{"jobsearch":jobsearch})
      else:
        # jobtitle=request.POST['jobtitle']s
        listofjob=PostedJob.objects.all().order_by('id').reverse()[:7]
        # skills=listofjob.email
        print("SKILLSSSS",listofjob)
        # print("INSIDE REDIRECT")
        # redirect("/alljobs")
        #  return render(request,'index.html')  
        return render(request,'index.html',{"listofjob":listofjob})
      return render(request,'index.html')       
    

def signup(request):
    return render(request,'signup.html')    

def employerdashboard(request):
    if request.user.is_authenticated:
        employerid=request.user.employerid
        joblist=PostedJob.objects.filter(employerid=employerid).order_by('id').reverse()
        countlist=PostedJob.objects.filter(employerid=employerid).count()
        print("COUNTLISTTTTT",countlist)
        print("COUNTLISTTTTT",joblist)
        # return render(request,'empalljobs.html',{"listofjob":joblist})  
        # return render(request,'employerdashboard.html',{"listofjob":joblist,"countlist":countlist})
        return render(request,'employerdashboard.html',{"listofjob":joblist})
    else:
        return render(request,'employeelogin.html')       


def postnewjob(request):
 if request.user.is_authenticated:
    username=request.user.username
    email=request.user.email
    ids=IdInformations.objects.get(username=username,email=email)
    employerid=ids.employerid
    profilecheck=EmployerContact.objects.filter(Fullname=username,email=email,employerid=employerid).exists()
    print("PROFILE CHECKKKK",profilecheck)
    if request.method=='GET':
        if 'Admin' == request.user.username:
            options=Skills.objects.all()
            return render(request,'adminpostjob.html',{"options":options})
        else:
            options=Skills.objects.all()
            return render(request,'postnewjob.html',{"profilecheck":profilecheck,"options":options})
    #    employerid=request.user.employerid
    else:
       if 'Admin' == request.user.username:
        jobtitle=request.POST.get('jobtitle',False)
        companyname=request.POST.get('companyname',False)
        companylogo=request.FILES['companylogo']
        joblink=request.POST.get('joblink',False)
        Description=request.POST.get('Description',False)
        jobcategory=request.POST.get('jobcategory',False)
        jobtype=request.POST.get('jobtype',False)
        joblevel=request.POST.get('joblevel',False)
        salaryfrom=request.POST.get('salaryfrom',False)
        salaryto=request.POST.get('salaryto',False)
        experience=request.POST.get('experience',False)
        language1=request.POST.get('language1',False)
        language2=request.POST.get('language2',False)
        language3=request.POST.get('language3',False)
        url=request.POST.get('url',False)
        companyemail=request.POST.get('companyemail',False)
        datetime=request.POST.get('datetime',False)
        skills=request.POST.get('skills',False)
        address=request.POST.get('address',False)
        jobsave=PostedJob.objects.create(jobtitle=jobtitle,companyname=companyname,companylogo=companylogo,description=Description,jobcategory=jobcategory,jobtype=jobtype,joblevel=joblevel,salaryfrom=salaryfrom,salaryto=salaryto,experience=experience,language1=language1,language2=language2,language3=language3,url=url,email=companyemail,date=datetime,skills=skills,location=address,employerid=employerid,joblinks=joblink)
        # jobsave=PostedJob.objects.create(jobtitle=jobtitle,companyname=companyname,companylogo=companylogo,joblinks=joblink,employerid=employerid)
        jobsave.save()
       else:
        jobtitle=request.POST.get('jobtitle',False)
        companyname=request.POST.get('companyname',False)
    #    companylogo=request.POST.get('companylogo',False)
        companylogo=request.FILES['companylogo']
        Description=request.POST.get('Description',False)
        jobcategory=request.POST.get('jobcategory',False)
        jobtype=request.POST.get('jobtype',False)
        # joblevel=request.POST.get('joblevel',False)
        openings=request.POST.get('openings',False)
        salaryfrom=request.POST.get('salaryfrom',False)
        salaryto=request.POST.get('salaryto',False)
        experience=request.POST.get('experience',False)
    #    language=request.POST.get('language',False)
    #    language=request.POST.getlist('language[]')
        # language1=request.POST.get('language1',False)
        # language2=request.POST.get('language2',False)
        # language3=request.POST.get('language3',False)
        # url=request.POST.get('url',False)
        # companyemail=request.POST.get('companyemail',False)
        # datetime=request.POST.get('datetime',False)
    #    skills=request.POST.getlist('skills[]')
        skills=request.POST.get('skills',False)
        address=request.POST.get('address',False)
    #    id=IdInformations.objects.get(companyname=companyname)
    #    employerid=id.employerid
        username=request.user.username
        email=request.user.email
        ids=IdInformations.objects.get(username=username,email=email)
        employerid=ids.employerid
        jobsave=PostedJob.objects.create(jobtitle=jobtitle,companyname=companyname,companylogo=companylogo,description=Description,jobcategory=jobcategory,jobtype=jobtype,openings=openings,salaryfrom=salaryfrom,salaryto=salaryto,experience=experience,skills=skills,location=address,employerid=employerid,username=username,email=email)
        # jobsave=PostedJob.objects.create(jobtitle=jobtitle,companyname=companyname,companylogo=companylogo,description=Description,jobcategory=jobcategory,jobtype=jobtype,joblevel=joblevel,salaryfrom=salaryfrom,salaryto=salaryto,experience=experience,language1=language1,language2=language2,language3=language3,url=url,email=companyemail,date=datetime,skills=skills,location=address,employerid=employerid)
        jobsave.save()
        messages.success(request,'Job has been posted Successfully')
    #    return render(request,'postnewjob.html',{"profilecheck":profilecheck})   
       return redirect('postnewjob')
    # return render(request,'postnewjob.html')        
    # messages.info(request,'Check Username and Password')
 else:
    return render(request,'employeelogin.html')       

def empalljobs(request):
 if request.user.is_authenticated:
    employerid=request.user.employerid
    if request.method=='POST':
        searchname=request.POST['searchname']
        jobstatus=request.POST['jobstatus']
        employerid=request.user.employerid
        joblist=PostedJob.objects.filter(jobtitle__iexact=searchname,jobtype__iexact=jobstatus,employerid=employerid).order_by('date').reverse()
        countlist=PostedJob.objects.filter(jobtitle__iexact=searchname,jobtype__iexact=jobstatus,employerid=employerid).count()
        print("JOBBBBBBBBBBB",joblist,countlist)
        return render(request,'empalljobs.html',{"listofjob":joblist,"countlist":countlist})
    else:
        joblist=PostedJob.objects.filter(employerid=employerid).order_by('id').reverse()
        countlist=PostedJob.objects.filter(employerid=employerid).count()
        return render(request,'empalljobs.html',{"listofjob":joblist,"countlist":countlist})    
 else:
    return render(request,'employeelogin.html')



def applicantlist(request):
     if request.user.is_authenticated:
        companyname=request.user.companyname
        # print(employerid)
        # companyname=PostedJob.objects.filter(employerid=employerid).first()
        # name=companyname.companyname
        applicantlist=AppliedJobs.objects.filter(companyname=companyname)
        countlist=AppliedJobs.objects.filter(companyname=companyname).count()
        print(applicantlist)
        return render(request,'applicantlist.html',{"applicantlist":applicantlist,"countlist":countlist})
     else:
        return render(request,'employeelogin.html')
         


def viewedresume(request):
    if request.user.is_authenticated:
     return render(request,'viewedresume.html')
    else:
        return render(request,'employeelogin.html')    


def empfilledprofile(request):
    if request.user.is_authenticated:
     return render(request,'empfilledprofile.html') 
    else:
        return render(request,'employeelogin.html') 


def empeditprofile(request):
 if request.user.is_authenticated:
    companyname=request.user.companyname
    username=request.user.username
    email=request.user.email
    empdetails=User.objects.filter(companyname=companyname,email=email)
    print("COMPANY NAME",request.user.companyname)
    empdetailss=IdInformations.objects.get(companyname=companyname,email=email)
    employerid=empdetailss.employerid
    if request.method =='GET':
    #  employerid=request.user.employerid
     companyname=request.user.companyname
     username=request.user.username
    #  print("employeridddd",employerid)
     empdetails=User.objects.filter(companyname=companyname)
     empdetailss=IdInformations.objects.get(companyname=companyname)
     employerid=empdetailss.employerid
     print(empdetails)
     print("employeridddd222222",employerid)
    #  if EmployeeProfile.objects.filter(Fullname=username).exists():
     if EmployerContact.objects.filter(Fullname=username).exists():
        print("EMPLOYEEECONTACCTTTTT")   
        # empfilled=EmployeeProfile.objects.filter(Fullname=username,employerid=employerid)
        empfilled=EmployerContact.objects.filter(Fullname=username,employerid=employerid)
        return render(request,'empfilledprofile.html',{"empfilled":empfilled})
     else:   
        return render(request,'empeditprofile.html',{"empdetails":empdetails})
        #   return render(request,'empeditprofile.html')
    else:
        # empname=request.POST.get('empname',False)
        # empmail=request.POST.get('empmail',False) 
        # phoneno=request.POST.get('phoneno',False)
        # dateofbirth=request.POST.get('dateofbirth',False)
        # headlines=request.POST.get('headlines',False)
        # gender=request.POST.get('gender',False)
        # aboutcompany=request.POST.get('aboutcompany',False)
        # employeeaddress=request.POST.get('employeeaddress',False)
        # facebook=request.POST.get('facebook',False)
        # twitter=request.POST.get('twitter',False)
        # googleplus=request.POST.get('googleplus',False)
        # youtube=request.POST.get('youtube',False)
        # empdetails=EmployeeProfile.objects.create(Fullname=empname,email=empmail,gender=gender,phone=phoneno,dof=dateofbirth,Headlines=headlines,Aboutcompany=aboutcompany,joblocation=employeeaddress,faceebook=facebook,googleplus=googleplus,twitter=twitter,youtube=youtube,employerid=employerid)
        # empdetails.save()
        empname=request.POST.get('empname',False)
        empmail=request.POST.get('empmail',False) 
        phoneno=request.POST.get('phoneno',False)
        companyname=request.POST.get('companyname',False)
        empaddress=request.POST.get('empaddress',False)
        date=User.objects.get(username=username,email=email) 
        joined=date.date_joined
        print("JOINEDDDD",joined)
        empdetails=EmployerContact.objects.create(Fullname=empname,email=empmail,phone=phoneno,companyname=companyname,employerid=employerid,empaddress=empaddress)
        empdetails.save()
    return redirect('/')    
 else:
    return render(request,'employeelogin.html')               

def empeditableprofile(request):
  if request.user.is_authenticated:  
    Fullname=request.user.username
    email=request.user.email
    if request.method =='GET':
     Fullname=request.user.username
     email=request.user.email
    #  empdetails=EmployeeProfile.objects.filter(Fullname=Fullname,email=email)
     empdetails=EmployerContact.objects.filter(Fullname=Fullname,email=email)
     print(empdetails)
     return render(request,'empeditableprofile.html',{"empdetails":empdetails})
    else:
        # empname=request.POST.get('empname',False)
        # empmail=request.POST.get('empmail',False) 
        # phoneno=request.POST.get('phoneno',False)
        # dateofbirth=request.POST.get('dateofbirth',False)
        # headlines=request.POST.get('headlines',False)
        # gender=request.POST.get('gender',False)
        # aboutcompany=request.POST.get('aboutcompany',False)
        # employeeaddress=request.POST.get('employeeaddress',False)
        # facebook=request.POST.get('facebook',False)
        # twitter=request.POST.get('twitter',False)
        # googleplus=request.POST.get('googleplus',False)
        # youtube=request.POST.get('youtube',False)
        # empdetails=EmployeeProfile.objects.filter(Fullname=Fullname,email=email).update(Fullname=empname,email=empmail,gender=gender,phone=phoneno,dof=dateofbirth,Headlines=headlines,Aboutcompany=aboutcompany,joblocation=employeeaddress,faceebook=facebook,googleplus=googleplus,twitter=twitter,youtube=youtube)
        # name=User.objects.filter(username=Fullname,email=email).update(username=empname,email=empmail) 
        empname=request.POST.get('empname',False)
        empmail=request.POST.get('empmail',False) 
        phoneno=request.POST.get('phoneno',False)
        companyname=request.POST.get('companyname',False)
        empaddress=request.POST.get('empaddress',False)
        print("Company name",companyname)
        empdetails=EmployerContact.objects.filter(Fullname=Fullname,email=email).update(Fullname=empname,email=empmail,phone=phoneno,companyname=companyname,empaddress=empaddress)
        name=User.objects.filter(username=Fullname,email=email).update(username=empname,email=empmail)
        id=IdInformations.objects.filter(username=Fullname,email=email).update(username=empname,email=empmail) 
    return redirect('/postnewjob') 
  else:
    return render(request,'employeelogin.html')

def register(request):
    if request.method =='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email id Exists")
                return redirect('/register')
            else:
                id=+1
                data=IdInformations.objects.count()
                if data == 0:
                    LastInsertId=0
                    EmpInsertId=0
                    numeric='JS'+str(LastInsertIdd)
                    id=numeric
                    user=User.objects.create_user(username=username,password=password1,email=email,typeofjob='JobSeeker',userid=numeric,empid=EmpInsertId,jobsekerid=LastInsertIdd)
                    Ids=IdInformations.objects.create(username=username,email=email,typeofjob='JobSeeker',userid=numeric,empid=EmpInsertId,jobsekerid=LastInsertIdd)
                    user.save();
                    Ids.save();  
                    messages.info(request,'Successfully created')
                    mail_subject = 'Activate your account.'
                    email_template_name='loginform.html'
                    message = render_to_string('loginform.html', {
                            'user': user.email,
                            'username':user.username,
                            'domain': 'myjob.com.sg',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token':default_token_generator.make_token(user),
                            'protocol':'https'
                        })
                    send_mail(mail_subject, message, 'youremail', [email])
                    return redirect('/candidatelogin/')
                else:    
                 print("id is",id)
                 LastInsertId = (IdInformations.objects.last()).jobsekerid
                 EmpInsertId = (IdInformations.objects.last()).empid
                 print("lastjobsekerid",LastInsertId)
                 LastInsertIdd=LastInsertId + 1
                 numeric='JS'+str(LastInsertIdd)
                 print("numeric",numeric)
                 id=numeric
                 user=User.objects.create_user(username=username,password=password1,email=email,typeofjob='JobSeeker',userid=numeric,empid=EmpInsertId,jobsekerid=LastInsertIdd)
                 print(user)
                 user.save();
                 Ids=IdInformations.objects.create(username=username,email=email,typeofjob='JobSeeker',userid=numeric,empid=EmpInsertId,jobsekerid=LastInsertIdd)
                 Ids.save();
                 messages.info(request,'Successfully created')
                 mail_subject = 'Activate your account.'
                 email_template_name='loginform.html'
                 message = render_to_string('loginform.html', {
                            'user': user.email,
                            'username':user.username,
                            'domain': 'myjob.com.sg',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token':default_token_generator.make_token(user),
                            'protocol':'https'
                        })
                # to_email = form.cleaned_data.get('email')
                # email=EmailMessage(mail_subject, message, 'youremail', [email])
                # return HttpResponse('Please confirm your email address to complete the registration')
                send_mail(mail_subject, message, 'youremail', [email])  
                return redirect('/candidatelogin/')
        else:
             messages.info(request,"Password not match")
             return redirect('/register')          
    return render(request,'register.html')

# def empregister(request):
#     return render(request,'empregister.html')

def logout(request):
    # del request.session['jobsekerlogin']
    return redirect('/')

def emplogout(request):
    # del request.session['userlogin']
    return redirect('/')    

def browsecompany(request):
    if request.user.is_authenticated:
     return render(request,'browsecompany.html')
    else:
        return render(request,'employeelogin.html')         

def empregister(request):
    id=1
    if request.method =='POST':
     username=request.POST['username']
     password1=request.POST['password1']
     password2=request.POST['password2']
     email=request.POST['email']
     companyname=request.POST['companyname']
     if password1==password2:
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email id Exits")
            return redirect('/register')
        elif User.objects.filter(companyname=companyname).exists():
            print("INSIDE THE COMPANY NAME")
            messages.info(request,"Company name Exits")
            return redirect('/register')    
        else:
            id=id+1
            # data=User.objects.count()
            data=IdInformations.objects.count()
            print("dataaa",data)
            if data ==0:
                LastInsertId=0
                jobsekerid=0
                print("lastinsertidddd",LastInsertId)
                numeric='EMP'+str(LastInsertId)
                id=numeric
                user=User.objects.create_user(username=username,password=password1,email=email,typeofjob='Employeer',employerid=numeric,empid=LastInsertId,jobsekerid=jobsekerid,companyname=companyname)        
                print("id",id)
                user.save();
                Ids=IdInformations.objects.create(username=username,email=email,typeofjob='Employeer',employerid=numeric,empid=LastInsertIdd,jobsekerid=jobsekerid,companyname=companyname)        
                Ids.save();
                messages.info(request,'SuccessFully created')
                mail_subject = 'Activate your account.'
                email_template_name='employeeform.html'
                message = render_to_string('employeeform.html', {
                            'user': user.email,
                            'username':user.username,
                            'domain': 'myjob.com.sg',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token':default_token_generator.make_token(user),
                            'protocol':'https'
                        })
                # send_mail(mail_subject, message, 'settings.FROM_EMAIL', [email])
                send_mail(mail_subject, message, 'youremail', [email])  
                return redirect('/employeelogin/')
            else:
              print("the id issss..",id)      
              LastInsertId = (IdInformations.objects.last()).empid
              jobsekerid = (IdInformations.objects.last()).jobsekerid
              print("lastinsertidddd",LastInsertId)
              LastInsertIdd=LastInsertId + 1
              numeric='EMP'+str(LastInsertIdd)
              id=numeric
              user=User.objects.create_user(username=username,password=password1,email=email,typeofjob='Employeer',employerid=numeric,empid=LastInsertIdd,jobsekerid=jobsekerid,companyname=companyname)        
              print("id",id)
              user.save();
              Ids=IdInformations.objects.create(username=username,email=email,typeofjob='Employeer',employerid=numeric,empid=LastInsertIdd,jobsekerid=jobsekerid,companyname=companyname)        
              Ids.save();
              mail_subject = 'Activate your account.'
              email_template_name='employeeform.html'
              message = render_to_string('employeeform.html', {
                            'user': user.email,
                            'username':user.username,
                            'domain': 'myjob.com.sg',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token':default_token_generator.make_token(user),
                            'protocol':'https'
                        })
              send_mail(mail_subject, message, 'youremail', [email])            
            #   send_mail(mail_subject, message,'myjobsg.com@gmail.com', [email],fail_silently=True)
              messages.info(request,'SuccessFully Created')
              print("mailll",email)
              return redirect('/employeelogin/') 
     else:
        messages.info(request,"Password not match")
        return redirect('/register')
    else:            
      return render(request,'empregister.html')

def candidatelogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            # request.session['jobsekerlogin'] = True
            # request.session['userlogin'] = True
            if User.objects.filter(username=username,typeofjob="JobSeeker"):
                request.session['jobsekerlogin'] = True
                print("SESSION",request.session['jobsekerlogin'])
                auth.login(request,user)
                nxt = request.GET.get("next", None)
                print("NEXT",nxt)
                url = '/candidateddashboard/'
                if nxt is not None:
                    url = nxt
                    print("URL",url)
                # next = request.POST.get('next','candidateddashboard')
                # return HttpResponseRedirect(next)
                # return redirect(next)
                # return redirect(request.GET.get('next',''))
                # next_param = request.POST.get('next')
                # if next_param:
                #   url = next_param
                # else:
                #     url = '/candidateddashboard/' 
                # return redirect(request.POST.get('next','candidateddashboard'))
                return redirect(url)
                # return redirect(url)
            else:
                messages.info(request,'Check Your Type of Job')
                return redirect('/candidatelogin/')
        else:
            print("INSIDE THE ELSE LOGINNNNNN",user)
            messages.info(request,'Check Username and Password')
            return redirect('/candidatelogin/')
    else:            
     return render(request,'candidatelogin.html')

def employeelogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if User.objects.filter(username=username,typeofjob="Employeer"):
             request.session['userlogin'] = True
             auth.login(request,user)
             return redirect('/employerdashboard/')
            else:
                messages.info(request,'Check Your Type of Job')
                return render(request,'employeelogin.html')
            # return render(request,'employerdashboard.html')
        else:
             messages.info(request,'Check Username and Password')
             return redirect('/employeelogin/') 
    else:
      return render(request,'employeelogin.html')     


def jobedit(request,id):
  if request.user.is_authenticated:
#    if request.method =='GET':
    #  joblist=PostedJob.objects.filter(jobtitle=jobtitle)
    if request.method =='POST':
    #    employerid=request.user.employerid
       jobtitle=request.POST.get('jobtitle',False)
       companyname=request.POST.get('companyname',False)
    #    companylogo=request.FILES['companylogo']
       Description=request.POST.get('Description',False)
       jobcategory=request.POST.get('jobcategory',False)
       jobtype=request.POST.get('jobtype',False)
       joblevel=request.POST.get('joblevel',False)
       salaryfrom=request.POST.get('salaryfrom',False)
       salaryto=request.POST.get('salaryto',False)
       experience=request.POST.get('experience',False)
    #    language=request.POST.getlist('language[]')
       language1=request.POST.get('language1',False)
       language2=request.POST.get('language2',False)
       language3=request.POST.get('language3',False)
       url=request.POST.get('url',False)
       companyemail=request.POST.get('companyemail',False)
       datetime=request.POST.get('datetime',False)
       skills=request.POST.getlist('skills[]')
       address=request.POST.get('address',False)
       jobsave=PostedJob.objects.filter(id=id).update(jobtitle=jobtitle,companyname=companyname,description=Description,jobcategory=jobcategory,jobtype=jobtype,joblevel=joblevel,salaryfrom=salaryfrom,salaryto=salaryto,experience=experience,language1=language1,language2=language2,language3=language3,url=url,email=companyemail,date=datetime,skills=skills,location=address)
       print("job saveddddd",jobsave)
       print("jobtitle",jobtitle)
       return render(request,'empalljobs.html')
    else:
        joblist=PostedJob.objects.filter(id=id)         
        return render(request,'jobedit.html',{"joblist":joblist}) 
  else:
    return render(request,'employeelogin.html') 


def emppasswordchange(request):
  if request.user.is_authenticated:  
    if request.method=='POST':
        name=request.user.username
        password=request.POST.get('newpassword',False)
        passwordnewconf=request.POST.get('newpasswordconfi',False)
        if password == passwordnewconf:
            u = User.objects.get(username=name)
            u.set_password(request.POST['newpassword'])
            u.save()
    return render(request,'emppasswordchange.html')
  else:
     return render(request,'employeelogin.html')

def jobsearch(request):
 if request.method=='GET':
  print("INSIDE THE JOBBBB SEARCHHHHH..........")
#   search_str=json.loads(request.body).get('searchText')
#   expenses=PostedJob.objects.filter(
#     jobtitle__istartswith=search_str) | PostedJob.objects.filter(jobtitle__icontains=search_str)
#   data=expenses.values()
#   print("dataaa",data)
#   return JsonResponse(list(data),safe=False)
#   jobtitle=request.POST['jobtitle']
  query=request.GET.get('jobtitle','')
  print("queryyyy222",query)
  if len(query)>0:
   jobsearch=PostedJob.objects.all().filter(Q(jobtitle__iexact=query) | Q(jobtitle__icontains=query) |Q(jobtitle__startswith=query)).distinct('jobtitle')
   print("queryyy",jobsearch)
   return render(request,'jobsearch.html',{"jobsearch":jobsearch})
  else:
    jobsearch=PostedJob.objects.all().order_by('id').reverse()
    return render(request,'jobsearch.html',{"jobsearch":jobsearch})
    print("searchhhh") 
 else:
    jobsearch=PostedJob.objects.all().order_by('id').reverse(),7
    # paginator=Paginator(jobsearch,6)
    # page=request.GET.get('page')
    # try:
    #     jobsearch=paginator.page(page)
    # except PageNotAnInteger:
    #     jobsearch=paginator.page(1)
    # except EmptyPage:
    #     jobsearch=paginator.page(paginator.num_pages)        
    # page=request.GET.get('page')
    # jobsearch=jobsearch1.get_page(page)
    return render(request,'jobsearch.html',{"jobsearch":jobsearch})   

    # print("all jobssssss 222222")
    # if request.method=='POST':
    #     jobtitle=request.POST['jobtitle']
    #     listofjob=PostedJob.objects.filter(jobtitle__iexact=jobtitle)
    #     # redirect('/alljobs')
    #     print("INSIDE THE ALLJOBS....")
    # print("INSIDE THE ALLL JOBBBBBBB")
    

def jobdetail(request,id):
    if request.user.is_authenticated:
    #  employerid=request.user.employerid
     email=request.user.email
    #  jobfull=PostedJob.objects.filter(id=id,employerid=employerid)
    #  jobform=EmployeeProfile.objects.filter(employerid=employerid)
     jobfull=PostedJob.objects.filter(id=id)
     jobform=EmployeeProfile.objects.filter(email=email)
     print("jobfull",jobfull)
     return render(request,'jobdetail.html',{"jobfull":jobfull})
    else:
        return render(request,'employeelogin.html')


def jobsekersearch(request):
    if request.method=='POST':
        searchname=request.POST['searchname']
        jobstatus=request.POST['jobstatus']
        jobsearch=PostedJob.objects.filter(jobtitle__iexact=searchname,jobtype__iexact=jobstatus)
        return render(request,'jobsekersearch.html',{"jobsearch":jobsearch})   
    else:    
     jobsearch=PostedJob.objects.all()
     return render(request,'jobsekersearch.html',{"jobsearch":jobsearch})        

def jobsekerpasswordchange(request):
  if request.user.is_authenticated:
    if request.method=='POST':
        name=request.user.username
        password=request.POST.get('newpassword',False)
        passwordnewconf=request.POST.get('newpasswordconfi',False)
        if password == passwordnewconf:
             u = User.objects.get(username=name)
             u.set_password(request.POST['newpassword'])
             u.save()
    return render(request,'jobsekerpasswordchange.html')
  else:
    return render(request,'candidatelogin.html')


def applyjob(request,jobtitle,id):
  if request.user.is_authenticated:   
    listofjob=PostedJob.objects.filter(id=id)
    listofjob1=PostedJob.objects.get(id=id)
    employerid=listofjob1.employerid
    joblink=listofjob1.joblinks
    jobform=EmployeeProfile.objects.filter(employerid=employerid)
    jobtitle=listofjob1.jobtitle
    email=request.user.email
    jobseekerprofile=JobsekerProfile.objects.filter(email=email).exists()
    print("jobseekerprofile",jobseekerprofile)
    if AppliedJobs.objects.filter(email=email,flag='1',jobtitle=jobtitle,deleteflag='0').exists():
        applylist=AppliedJobs.objects.filter(email=email,flag='1',jobtitle=jobtitle,deleteflag='0').exists()
        savedlist=CandidateSaved.objects.filter(email=email,flag='1',jobtitle=jobtitle).exists()
        # hitcount=PostedJob.objects.filter(id=id).update(hitcount=F('hitcount')+1)
        print("inside the applylist if ",applylist)
        meta_title=jobtitle
        meta_description=listofjob1.description
        category=listofjob1.jobcategory
        return render(request,'applyjob.html',{"listofjob":listofjob,"jobform":jobform,"listapply":applylist,"savedlist":savedlist,"jobseekerprofile":jobseekerprofile,"joblink":joblink,"meta_title":meta_title,"meta_description":meta_description,"category":category})
    else:
        blankflag=1
        applylist=AppliedJobs.objects.filter(email=email,flag='1',jobtitle=jobtitle,deleteflag='0').exists()
        savedlist=CandidateSaved.objects.filter(email=email,flag='1',jobtitle=jobtitle).exists()
        # hitcount=PostedJob.objects.filter(id=id).update(hitcount=F('hitcount')+1)
        print("inside the applylist elseeee",applylist)
        meta_title=jobtitle
        meta_description=listofjob1.description
        meta_companyname=listofjob1.companyname
        category=listofjob1.jobcategory
        print("METAAAAA",meta_companyname)
        return render(request,'applyjob.html',{"listofjob":listofjob,"jobform":jobform,"listapply":applylist,"blankflag":blankflag,"jobseekerprofile":jobseekerprofile,"savedlist":savedlist,"joblink":joblink,"meta_title":meta_title,"meta_description":meta_description,"meta_companyname":meta_companyname,"category":category})
  else:
    listofjob=PostedJob.objects.filter(id=id)
    listofjob1=PostedJob.objects.get(id=id)
    employerid=listofjob1.employerid
    joblink=listofjob1.joblinks
    jobform=EmployeeProfile.objects.filter(employerid=employerid)
    jobtitle=listofjob1.jobtitle
    meta_title=jobtitle
    meta_description=listofjob1.description.replace("\n", " ")
    # meta_description=listofjob1.description.replace(" ", "")
    category=listofjob1.jobcategory
    print("META DESCRIPTIONNNN",meta_description)
    # hitcount=PostedJob.objects.filter(id=id).update(hitcount=F('hitcount')+1)
    return render(request,'applyjob.html',{"listofjob":listofjob,"jobform":jobform,"meta_title":meta_title,"meta_description":meta_description,"category":category})  
 


# def applyjob(request,id):
#   if request.user.is_authenticated:   
#     listofjob=PostedJob.objects.filter(id=id)
#     listofjob1=PostedJob.objects.get(id=id)
#     employerid=listofjob1.employerid
#     joblink=listofjob1.joblinks
#     jobform=EmployeeProfile.objects.filter(employerid=employerid)
#     jobtitle=listofjob1.jobtitle
#     email=request.user.email
#     jobseekerprofile=JobsekerProfile.objects.filter(email=email).exists()
#     print("jobseekerprofile",jobseekerprofile)
#     if AppliedJobs.objects.filter(email=email,flag='1',jobtitle=jobtitle,deleteflag='0').exists():
#         applylist=AppliedJobs.objects.filter(email=email,flag='1',jobtitle=jobtitle,deleteflag='0').exists()
#         savedlist=CandidateSaved.objects.filter(email=email,flag='1',jobtitle=jobtitle).exists()
#         print("inside the applylist if ",applylist)
#         return render(request,'applyjob.html',{"listofjob":listofjob,"jobform":jobform,"listapply":applylist,"savedlist":savedlist,"jobseekerprofile":jobseekerprofile,"joblink":joblink})
#     else:
#         blankflag=1
#         applylist=AppliedJobs.objects.filter(email=email,flag='1',jobtitle=jobtitle,deleteflag='0').exists()
#         savedlist=CandidateSaved.objects.filter(email=email,flag='1',jobtitle=jobtitle).exists()
#         print("inside the applylist elseeee",applylist)
#         return render(request,'applyjob.html',{"listofjob":listofjob,"jobform":jobform,"listapply":applylist,"blankflag":blankflag,"jobseekerprofile":jobseekerprofile,"savedlist":savedlist,"joblink":joblink})
#   else:
#     return render(request,'candidatelogin.html')   


def jobapplied(request,id):
  if request.user.is_authenticated: 
    jobapplied=PostedJob.objects.get(id=id)
    jobtitle=jobapplied.jobtitle
    jobtype=jobapplied.jobtype
    username=request.user.username
    email=request.user.email
    companyname=jobapplied.companyname
    employerid=jobapplied.employerid
    userid=request.user.userid
    username=request.user.username
    email=request.user.email
    ids=IdInformations.objects.get(username=username,email=email)
    ids=IdInformations.objects.get(email=email)
    userid=ids.userid
    if JobsekerProfile.objects.filter(fullname=username).exists():
        jobseker=JobsekerProfile.objects.get(fullname=username)
        resume=jobseker.fileupload
        address=jobseker.address
        experience=jobseker.experience
        # skills=jobseker.skills
        currentjob=jobseker.currentjob
        applyjob=AppliedJobs.objects.create(jobtitle=jobtitle,jobtype=jobtype,email=email,username=username,status="Applied",companyname=companyname,flag='1',fileupload=resume,employerid=employerid,userid=userid,address=address,experience=experience,currentjob=currentjob)
        applyjob.save()
        # return redirect('jobsekersearch')
        # return render(request,'jobapplied.html')
        # return render(request,'applyjob.html')
        return redirect('applyjob',jobtitle,id)
    else:
        emptyflag=1
        return render(request,'jobapplied.html')
  else:
    return render(request,'candidatelogin.html')      

def profiledetails(request,username,jobtitle):
   if request.user.is_authenticated: 
    if request.method=='POST':
        positionofjob=request.POST.get('positionofjob',False)
        profiledisplay=JobsekerProfile.objects.get(fullname=username)
        hire=AppliedJobs.objects.filter(username=username,jobtitle=jobtitle).update(status=positionofjob)
        print(hire)
        profilelist=AppliedJobs.objects.filter(username=username,jobtitle=jobtitle)
        # return render(request,'profiledetails.html',{"profilelist":profilelist})
        return redirect("/applicantlist/")
    else:
      profilelist=AppliedJobs.objects.filter(username=username,jobtitle=jobtitle)
      authuser=User.objects.filter(username=username)
      return render(request,'profiledetails.html',{"profilelist":profilelist,"authuser":authuser})
   else:
      return render(request,'employeelogin.html')   

def candidatefilledform(request):
    if request.user.is_authenticated:
     username=request.user.username
     userid=request.user.userid
     filledprofile=JobsekerProfile.objects.filter(fullname=username)
     return render(request,'candidatefilledform.html')
    else:
        return render(request,'candidatelogin.html')       


def freeapplysearch(request,id):
    listofjob=PostedJob.objects.filter(id=id)
    listofjob1=PostedJob.objects.get(id=id)
    employerid=listofjob1.employerid
    jobform=EmployeeProfile.objects.filter(employerid=employerid)
    jobtitle=listofjob1.jobtitle
    # email=request.user.email
    # if AppliedJobs.objects.filter(email=email,flag='1',jobtitle=jobtitle).exists():
        # applylist=AppliedJobs.objects.filter(email=email,flag='1',jobtitle=jobtitle).exists()
        # print("inside the applylist if ",applylist)
        # return render(request,'applyjob.html',{"listofjob":listofjob,"jobform":jobform,"listapply":applylist})
    return render(request,'freeapplysearch.html',{"listofjob":listofjob,"jobform":jobform})       

def contactus(request):
    return render(request,'contactus.html')

def password_reset_request(request):
    if request.method=='POST':
        password_form=PasswordResetForm(request.POST)
        if password_form.is_valid():
         data=password_form.cleaned_data['email']
         user_email=User.objects.filter(Q(email=data))
         if user_email.exists():
            for user in user_email:
                subject='Password Resquest'
                email_template_name='password_message.txt'
                parameters={
                    'email':user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name':'Myjob',
                    # 'uid':urlsafe_b64encode(force_bytes(user.pk)),
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':default_token_generator.make_token(user),
                    'protocol':'http'
                }
                print("the mail is",user.email)
                email=render_to_string(email_template_name,parameters)
                print(email)
                print(subject)
                # try:
                send_mail(subject,email,'',[user.email],fail_silently=False)
                    #  send_mail("Hello","Your Password Link",'subashdhanush1618@gmail.com',['subashweb03@gmail.com'])
                # except:
                #     return HttpResponse('Invalid Header')
                return redirect('/password_reset_done')         
    else:
        password_form=PasswordResetForm()    
    context={
       'password_form':password_form,
    }
    return render(request,'password_reset.html',context)

def password_reset_confirm(request):
    print("INSIDE THE PASSWORD RESET")
    if request.method=='POST':
        return render(request,'password_reset_complete.html')

       
def candidatesavedjobs(request,id):
 if request.user.is_authenticated:  
    jobapplied=PostedJob.objects.get(id=id)
    jobtitle=jobapplied.jobtitle
    jobtype=jobapplied.jobtype
    companyname=jobapplied.companyname
    email=jobapplied.email
    employerid=jobapplied.employerid
    expirydate=jobapplied.date
    username=request.user.username
    email=request.user.email
    salaryfrom=jobapplied.salaryfrom
    salaryto=jobapplied.salaryto
    ids=IdInformations.objects.get(email=email,username=username)
    userid=ids.userid
    username=ids.username
    print("EXPIRY DATEEE",expirydate)
    candidatesaved=CandidateSaved.objects.create(jobtitle=jobtitle,jobtype=jobtype,status='Saved',email=email,companyname=companyname,flag='1',employerid=employerid,userid=userid,username=username,salaryfrom=salaryfrom,salaryto=salaryto,expirydate=expirydate)
    candidatesaved.save()
    return redirect('applyjob',jobtitle,id)
    # return render(request,'candidatesavedjobs.html')       
 else:
    return render(request,'candidatelogin.html')

def aboutus(request):
    return render(request,'aboutus.html')    

def Logout(request):
    # try:
    #     del request.session['userlogin']
    # except KeyError:
    #     pass
    # print("SEEEEEEEEEEEE",request.session['userlogin'])
    # return HttpResponse("You're logged out.")
    # del request.session['userlogin']
    # request.session['userlogin'] = False
    request.session.clear()
    return redirect('/')    

def jobsekerLogout(request):
    # try:
    #     del request.session['jobsekerlogin']
    # except KeyError:
    #     pass
    # return HttpResponse("You're logged out.")
    # request.session['jobsekerlogin'] = False
    # del request.session['jobsekerlogin']
    request.session.clear()
    return redirect('/')    


def candidatededitresume(request):
 if request.user.is_authenticated:  
    fullname=request.user.username
    email=request.user.email
    ids=IdInformations.objects.get(username=fullname,email=email)
    userid=ids.userid
    profileedit=JobsekerProfile.objects.filter(userid=userid,fullname=fullname,email=email).exists()
    print("PROFILEEDITTTTT",profileedit)
    profile=JobsekerProfile.objects.filter(userid=userid,fullname=fullname,email=email)
    print("profileeeeeeeeeeeeeeeeee",profile)
    if request.method == 'POST':
        fullname=request.user.username
        email=request.user.email
        ids=IdInformations.objects.get(username=fullname,email=email)
        userid=ids.userid
        username=request.POST.get('username',False)
        qualification=request.POST.get('qualification',False)
        # resume=request.POST.get('resume',False)
        # resume=request.FILES['resume']
        jobcategory=request.POST.get('jobcategory',False)
        jobtype=request.POST.get('jobtype',False)
        singaporean=request.POST.get('singaporean',False)
        salaryfrom=request.POST.get('salaryfrom',False)
        # skills=request.POST.getlist('skills[]',False)
        experience=request.POST.get('experience',False)
        contactnumber=request.POST.get('contactnumber',False)
        email=request.POST.get('email',False)
        address=request.POST.get('address',False)
        userid=userid
        currentjob=request.POST.get('currentjob',False)
        seekerdetails=JobsekerProfile.objects.filter(userid=userid,fullname=fullname,email=email).update(Qualification=qualification,jobcategory=jobcategory,jobtype=jobtype,singaporean=singaporean,salaryfrom=salaryfrom,experience=experience,contactnumber=contactnumber,address=address,userid=userid,currentjob=currentjob)
        # seekerdetails=JobsekerProfile.objects.filter(userid=userid,fullname=fullname,email=email).update(Qualification=qualification,jobcategory=jobcategory,jobtype=jobtype,joblevel=joblevel,languages=language,salaryfrom=salaryfrom,skills=skills,experience=experience,contactnumber=contactnumber,address=address,location=location,currentjob=currentjob)
        # seekerdetails=JobsekerProfile.objects.filter(userid=userid,fullname=username,email=email).update(fullname=username,Qualification=qualification,jobcategory=jobcategory,jobtype=jobtype,joblevel=joblevel,languages=language,salaryfrom=salaryfrom,skills=skills,experience=experience,contactnumber=contactnumber,email=email,address=address,location=location)
        # seekerdetails=JobsekerProfile.objects.filter(fullname=username,email=email).update(Fullname=username,email=email,Qualification=qualification,gender=gender,phone=phoneno,dof=dateofbirth,Headlines=headlines,Aboutcompany=aboutcompany,joblocation=employeeaddress,faceebook=facebook,googleplus=googleplus,twitter=twitter,youtube=youtube)
        name=User.objects.filter(username=username,email=email).update(username=username,email=email)
        print("SEEKEERRRDETAILSSS",seekerdetails) 
    return render(request,'candidatededitresume.html',{"profile":profile,"profileedit":profileedit})    
 else:
      return render(request,'candidatelogin.html')


def loginform(request):
    rendered = render_to_string('loginform.html', {'username': request.user.username})
    # return render(request,'loginform.html')      

def jobdelete(request,id):
#   delete=PostedJob.objects.filter(id=id).update(deleteflag='1')
  deletejob =PostedJob.objects.get(id=id)
  deletejob.delete()
  messages.info(request,"Your Job is Deleted")
  return redirect('/empalljobs')    

def seekerdeletejob(request,id):
    seekerdelete=AppliedJobs.objects.get(id=id)
    delete=AppliedJobs.objects.filter(id=id).update(deleteflag='1')
    return redirect('/candidatedappliedjobs')

def adminpostjob(request):
    return render(request,'adminpostjob.html')

def contactus(request):
    if request.method=='POST':
        contactname=request.POST.get('contactname',False)
        contactemail=request.POST.get('contactemail',False)
        contactphonenumber=request.POST.get('contactphonenumber',False)
        contactsubject=request.POST.get('contactsubject',False)
        contactmessage=request.POST.get('contactmessage',False)
        contactsave=ContactDetail.objects.create(contactname=contactname,contactemail=contactemail,contactphonenumber=contactphonenumber,contactsubject=contactsubject,contactmessage=contactmessage)
        contactsave.save()
        mail_subject = 'myjob Enquiry'
        message = render_to_string('questionasked.html', {
                            'user': contactname,
                            'username':contactemail,
                            'message':contactmessage,
                            'domain': 'myjob.com.sg',
                        })
        send_mail(mail_subject, message, 'myjobsg.com@gmail.com', ['myjobsg.com@gmail.com'])                
        # send_mail('Question Asked', contactmessage, 'myjobsg.com@gmail.com', ['myjobsg.com@gmail.com'])
    return render(request,'contactus.html')




def payment(request):
  if request.method=='POST':  
    body = json.loads(request.body)
    user=request.user,
    payment_id=body['transID'],
    paypal_transaction_id=body['paypal_transaction_id'],
    payment_method=body['payment_method'],
    # amount_paid=order.order_total,
    status=body['status'],
    print("PAYMENTTTTTTT DETAILSSSS",paypal_transaction_id)
  return render(request,'payment.html')
    #  host=request.get_host()
    # payid=body['ID'],
    # print("PAYMMMMMMMMEEE",payid)
    # if request.method=='POST':
        # orderData=request.POST.get('orderData',False)
        # print("PAYMENTTTTT",orderData);
        # order = get_object_or_404(Order, id=ipn.invoice)
        # body = json.loads(request.body)
        # payment_id=body['transID'],
        # paypal_transaction_id=body['paypal_transaction_id'],
        # payment_method=body['payment_method'],
        # amount_paid=order.order_total,
        # status=body['status'],
        # print("PAYMENTTTT",payment_id,paypal_transaction_id,payment_method,status)
    
    #  paypal_dict = {
      
    #   'business': settings.PAYPAL_RECEIVER_EMAIL,
    #   'amount':'20.00',
    #   'item_name':'Product 1',
    #   'invoice':str(uuid.uuid4()),
    #   'currency_code':'USD',
    #   'notify_url':f'http://{host}{reverse("paypal-ipn")}',
    #   "notify_url": f'http://{host}(reverse("paypal-ipn"))',
    #   'return_url':f'http://{host}{reverse("paypal-return")}',
    #   'cancel_return':f'http://{host}{reverse("paypal-cancel")}',
    #  }
    #  form=PayPalPaymentsForm(initial=paypal_dict)
    #  context={'form':form}
    # return render(request,'payment.html')

def payment_complete(request):
    # PPClient=PayPalClient()
    # body=json.loads(request.body)
    # data=body["orderID"]
    # requestorder=OrdersGETRequest(data)
    return render(request,"payment_complete.html")


def paypal_return(request):
    messages.success(request,'You\'ve successfully made a payment!')
    return redirect('index')

def paypal_cancel(request):
    messages.error(request,'You\'re order has been cancelled!')
    return redirect('index')    


def payout(request):
    data=json.loads(request.body)
    # print("DATAAAAA",data)
    for key, value in data.items():
        paypal_id=value['id']
        payer_emailaddress=value['payer']['email_address']
        payer_id=value['payer']['payer_id']
        payee_emailaddress=value['purchase_units'][0]['payee']['email_address']
        currency_code=value['purchase_units'][0]['amount']['currency_code']
        amount=value['purchase_units'][0]['amount']['value']
        shippingaddress1=value['purchase_units'][0]['shipping']['address']['address_line_1']
        admin_area_1=value['purchase_units'][0]['shipping']['address']['admin_area_1']
        admin_area_2=value['purchase_units'][0]['shipping']['address']['admin_area_2']
        country_code=value['purchase_units'][0]['shipping']['address']['country_code']
        postal_code=value['purchase_units'][0]['shipping']['address']['postal_code']
    print("dataq",postal_code)
    # id=data['id']
    # print("IDDDDDDD",id)
    customer=request.user.username
    paysave=Payment_Details.objects.create(paypal_id=paypal_id,payer_emailaddress=payer_emailaddress,payer_id=payer_id,payee_emailaddress=payee_emailaddress,currency_code=currency_code,amount=amount,shippingaddress1=shippingaddress1,admin_area_1=admin_area_1,admin_area_2=admin_area_2,country_code=country_code,postal_code=postal_code)
    # name=data['orderData']
    paysave.save()
    return JsonResponse("It is working",safe=False)

def get_client_ip(request):
    x_forwarded_for=request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip=x_forwarded_for.split(',')[0]
    else:
        ip=request.META.get('REMOTE_ADDR')
    return ip      


def christsqaure(request):
    return render(request,'christsquare.html')

def songs(request):
    return render(request,'pagenotfound.html')
    

def adminlite(request):
    return render(request,'adminlite.html')

