from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.views.decorators.csrf import csrf_exempt




urlpatterns = [

path('',views.index,name='home'),
path('Logout/',views.Logout,name='Logout'),
path('signup/',views.signup,name='signup'),
path('employerdashboard/',views.employerdashboard,name='employerdashboard'),
path('postnewjob/',views.postnewjob,name='postnewjob'),    
path('empalljobs/',views.empalljobs,name='empalljobs'),
path('applicantlist/',views.applicantlist,name='applicantlist'),
path('viewedresume/',views.viewedresume,name='viewedresume'),  
path('empeditprofile/',views.empeditprofile,name='empeditprofile'),  
path('register/',views.register,name='register'),  
path('empregister/',views.empregister,name='empregister'),
path('candidateddashboard/',views.candidateddashboard,name='candidateddashboard'),
path('candidatedresume/',views.candidatedresume,name='candidatedresume'),
path('candidatededitresume/',views.candidatededitresume,name='candidatededitresume'),
path('candidatedappliedjobs/',views.candidatedappliedjobs,name='candidatedappliedjobs'),
path('candidatedsavedjobs/',views.candidatedsavedjobs,name='candidatedsavedjobs'),
path('alertjobs/',views.alertjobs,name='alertjobs'),
path('logout/',views.logout,name='logout'),
path('emplogout/',views.logout,name='emplogout'),
path('browsecompany/',views.browsecompany,name='browsecompany'),
path('candidatelogin/',views.candidatelogin,name='candidatelogin'),
path('employeelogin/',views.employeelogin,name='employeelogin'),
path('jobedit/<int:id>',views.jobedit,name='jobedit'),
path('empeditableprofile/',views.empeditableprofile,name='empeditableprofile'),  
path('emppasswordchange/',views.emppasswordchange,name='emppasswordchange'),  
path('empfilledprofile/',views.empfilledprofile,name='empfilledprofile'),
# path('jobsearch/',csrf_exempt(views.jobsearch),name='jobsearch'), 
path('jobsearch/',views.jobsearch,name='jobsearch'), 
path('jobdetail/<int:id>',views.jobdetail,name='jobdetail'),
path('jobsekersearch/',views.jobsekersearch,name='jobsekersearch'), 
path('jobsekerpasswordchange/',views.jobsekerpasswordchange,name='jobsekerpasswordchange'),
# path('jobs-in-singapore/<int:id>',views.applyjob,name='applyjob'),
path('jobs-in-singapore/<str:jobtitle>/<int:id>',views.applyjob,name='applyjob'),
path('jobapplied/<int:id>',views.jobapplied,name='jobapplied'),
path('profiledetails/<str:username>/<str:jobtitle>',views.profiledetails,name='profiledetails'),
path('candidatefilledform/',views.candidatefilledform,name='candidatefilledform'),
# path('singapore-jobs/<int:id>',views.freeapplysearch,name='freeapplysearch'),
path('singapore-jobs/<int:id>',views.freeapplysearch,name='freeapplysearch'),
path('contactus/',views.contactus,name='contactus'),
path('password_reset/', views.password_reset_request,name='password_reset'),
path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
path('candidatesavedjobs/<int:id>',views.candidatesavedjobs,name='candidatesavedjobs'),
path('aboutus/',views.aboutus,name='aboutus'),
path('jobsekerLogout/',views.jobsekerLogout,name='jobsekerLogout'),
path('jobdelete/<int:id>',views.jobdelete,name='jobdelete'),
path('seekerdeletejob/<int:id>',views.seekerdeletejob,name='seekerdeletejob'),
path('adminpostjob/',views.adminpostjob,name='adminpostjob'),
path('paypal-return',views.paypal_return,name='paypal-return'),
path('paypal-cancel',views.paypal_cancel,name='paypal-cancel'),
path('payment',views.payment,name='payment'),
path('payment_complete',views.payment_complete,name='payment_complete'),
path('payout',views.payout,name='payout'),
path('christsquare',views.christsqaure,name='christsquare'),
path('songs',views.songs,name='songs'),
path('adminlite',views.adminlite,name='adminlite')
# path('contactus/',views.contactus,name='contactus')
# path('save_profile/',views.save_profile,name="save_profile")      

      
# path('empbase/',views.empbase,name='empbase'),  






]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);