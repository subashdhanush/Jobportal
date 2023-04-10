import email
from email.policy import default
from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.urls  import reverse
from ckeditor.fields import RichTextField
# from django.contrib.auth.models import AbstractUser
# from jobportal.models import User





# Create your models here.
class User(AbstractUser):
    typeofjob=models.CharField(max_length=50,default=True)
    intrestcategory=models.CharField(max_length=100,default=True)
    userid=models.CharField(max_length=50,default=True)
    employerid=models.CharField(max_length=50,default='0')
    empid=models.IntegerField(default='0')
    jobsekerid=models.IntegerField(default='0')
    companyname=models.CharField(max_length=50,default='')
    def __str__(self):
        return self.username
    class Meta:
             db_table='auth_user'


class PostedJob(models.Model):
    jobtitle=models.CharField(max_length=100,default='')
    companyname=models.CharField(max_length=100,default='')
    companylogo=models.ImageField(upload_to='store/images',default='',blank=True)
    # description=models.CharField(max_length=5,default='')
    #description=models.TextField()
    description=RichTextField(blank=True,null=True)
    jobcategory=models.CharField(max_length=50,default='')
    jobtype=models.CharField(max_length=50,default='')
    openings=models.CharField(max_length=50,default='')
    # salaryfrom=models.IntegerField(default='1',blank=True)
    # salaryto=models.IntegerField(default='1',blank=True)
    salaryfrom=models.CharField(max_length=100,blank=True)
    salaryto=models.CharField(max_length=100,blank=True)
    experience=models.CharField(max_length=100,blank=True)
    # language1=models.CharField(max_length=500,default='')
    # language2=models.CharField(max_length=500,default='')
    # language3=models.CharField(max_length=500,default='')
    # url=models.CharField(max_length=150,default='')
    email=models.CharField(max_length=150,default='')
    # date=models.DateTimeField(auto_now_add=True)
    # date=models.DateField()
    skills=models.CharField(max_length=300,default='')
    location=models.CharField(max_length=500,default='')
    employerid=models.CharField(max_length=50,default='0')
    deleteflag=models.IntegerField(default='0')
    date_posted= models.DateTimeField(auto_now_add=True)
    joblinks=models.CharField(max_length=300,default='')
    username=models.CharField(max_length=300,default='')
    slug=models.SlugField(blank=True,null=True)
    # count_hit=models.ImageField(default='0')
    # views=models.ManyToManyField('IpModel',related_name="post_views",blank=True)
    # hitcount=models.IntegerField(default='0')
    # hit_count=models.IntegerField(default='0')
    # tags=TaggableManager()
    # class Meta:
    #     model = PostedJob
    #     fields = "__all__"

    def save(self,*args,**kwargs):
        self.slug=slugify(self.jobtitle)
        super().save(*args,**kwargs) 
    
    
    def get_absolute_url(self):
        return reverse('jobs-in-singapore', args=(slugify(self.jobtitle),))


    # def get_absolute_url(self):
    #     return reverse('jobs-in-singapore',kwargs={"slug":self.slug,"id":self.id})
    # def __str__(self):
    #     return self.jobtitle

    # def get_absolute_url(self):
    #     return f'/{self.slug}/'


    
class EmployeeDetails(models.Model):
    Fullname=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=150,default='')
    gender=models.CharField(max_length=50,default='')
    phone=models.IntegerField(default='1',blank=True)
    # DOB=models.DateField(default='1',blank=True)
    Headlines=models.CharField(max_length=150,default='')
    Aboutcompany=models.CharField(max_length=350,default='')
    joblocation=models.CharField(max_length=150,default='')
    faceebook=models.CharField(max_length=150,default='')
    twitter=models.CharField(max_length=150,default='')
    googleplus=models.CharField(max_length=150,default='')
    youtube=models.CharField(max_length=150,default='')
    dof=models.DateField(max_length=8)

class EmployeeProfile(models.Model):
    Fullname=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=150,default='')
    gender=models.CharField(max_length=50,default='')
    phone=models.BigIntegerField(default='1')
    Headlines=models.CharField(max_length=150,default='')
    Aboutcompany=models.CharField(max_length=350,default='')
    joblocation=models.CharField(max_length=150,default='')
    faceebook=models.CharField(max_length=150,default='')
    twitter=models.CharField(max_length=150,default='')
    googleplus=models.CharField(max_length=150,default='')
    youtube=models.CharField(max_length=150,default='')
    dof=models.DateField(max_length=8) 
    employerid=models.CharField(max_length=50,default='0')
    

class JobsekerProfile(models.Model):
     fullname = models.CharField(max_length=150,default='')
     Qualification= models.CharField(max_length=100,default='')
     fileupload=models.FileField(upload_to='store/pdfs',default='',blank=True)
     jobcategory=models.CharField(max_length=50,default='True')
     jobtype=models.CharField(max_length=50,default='')
     salaryfrom=models.IntegerField(default='1',blank=True)
     contactnumber=models.BigIntegerField(default='1',blank=True)
     email=models.CharField(max_length=150,default='')
     address=models.CharField(max_length=500,default='')
     userid=models.CharField(max_length=50,default='0')
     experience=models.CharField(max_length=100,blank=True)
     currentjob=models.CharField(max_length=150,default='')
     singaporean=models.CharField(max_length=150,default='')

    #  def __str__(self):
    #     return self.fullname




class AppliedJobs(models.Model):
     jobtitle=models.CharField(max_length=100,default='')
     jobtype=models.CharField(max_length=50,default='')
     status=models.CharField(max_length=50,default='')
     username=models.CharField(max_length=100,default='')
     email=models.CharField(max_length=100,default='')
     companyname=models.CharField(max_length=100,default='')
     flag=models.IntegerField(default='0')
     fileupload=models.FileField(upload_to='store/pdfs',default='',blank=True)
     employerid=models.CharField(max_length=50,default='0')
     userid=models.CharField(max_length=50,default='0')
     address=models.CharField(max_length=500,default='')
    #  date=models.DateField(max_length=8)
    #  date=models.DateTimeField(auto_now_add=True)
     skills=models.CharField(max_length=500,default='')
     currentjob=models.CharField(max_length=150,default='')  
     experience=models.CharField(max_length=100,blank=True)
     deleteflag=models.IntegerField(default='0')
     date=models.DateTimeField(auto_now_add=True)
    #  def __str__(self):
    #     return self.username 
     
class IdInformations(models.Model):
    username=models.CharField(max_length=100,default='')
    typeofjob=models.CharField(max_length=50,default=True)
    userid=models.CharField(max_length=50,default=True)
    employerid=models.CharField(max_length=50,default='0')
    empid=models.IntegerField(default='0')
    jobsekerid=models.IntegerField(default='0')
    companyname=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=150,default='')


class SavedJobs(models.Model):
    jobtitle=models.CharField(max_length=100,default='')
    jobtype=models.CharField(max_length=50,default='')
    status=models.CharField(max_length=50,default='')
    username=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    companyname=models.CharField(max_length=100,default='')
    flag=models.IntegerField(default='0')
    employerid=models.CharField(max_length=50,default='0')
    userid=models.CharField(max_length=50,default='0')    
    skills=models.CharField(max_length=500,default='')
    saveddate=models.DateField(max_length=8) 
    expirydate=models.DateTimeField(auto_now_add=True)


class CandidateSavedJobs(models.Model):
    jobtitle=models.CharField(max_length=100,default='')
    jobtype=models.CharField(max_length=50,default='')
    status=models.CharField(max_length=50,default='')
    username=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    companyname=models.CharField(max_length=100,default='')
    flag=models.IntegerField(default='0')
    employerid=models.CharField(max_length=50,default='0')
    userid=models.CharField(max_length=50,default='0')    
    skills=models.CharField(max_length=500,default='')
    saveddate=models.DateField(max_length=8,default='0') 
    expirydate=models.DateTimeField(auto_now_add=True)
    datesaved=models.DateTimeField(auto_now_add=True)
    salaryfrom=models.IntegerField(default='1',blank=True)
    salaryto=models.IntegerField(default='1',blank=True) 

     
class CandidateSaved(models.Model):
    jobtitle=models.CharField(max_length=100,default='')
    jobtype=models.CharField(max_length=50,default='')
    status=models.CharField(max_length=50,default='')
    username=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    companyname=models.CharField(max_length=100,default='')
    flag=models.IntegerField(default='0')
    employerid=models.CharField(max_length=50,default='0')
    userid=models.CharField(max_length=50,default='0')    
    skills=models.CharField(max_length=500,default='')
    expirydate=models.DateTimeField(auto_now_add=True)
    salaryfrom=models.IntegerField(default='1',blank=True)
    salaryto=models.IntegerField(default='1',blank=True) 

     
class EmployerContact(models.Model):
    Fullname=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=150,default='')
    phone=models.BigIntegerField(default='1')
    companyname=models.CharField(max_length=150,default='')
    employerid=models.CharField(max_length=50,default='0')
    empaddress=models.TextField(default='')
    # dateofjoined=models.CharField(max_length=100,blank=True)
    # dateofjoined=models.DateField(max_length=20,default=datetime.now) 
    def __str__(self):
        return self.Fullname
     

class ContactDetail(models.Model):
    contactname=models.CharField(max_length=100,default='')
    contactemail=models.CharField(max_length=150,default='')
    contactphonenumber=models.BigIntegerField(default='1')
    contactsubject=models.CharField(max_length=150,default='')
    contactmessage=models.TextField()



class Skills(models.Model):
    skillsrequired=models.CharField(max_length=500)
    def __str__(self):
        return self.skillsrequired   


class Payment_Details(models.Model):
    paypal_id=models.CharField(max_length=150,default=True)
    payer_emailaddress=models.CharField(max_length=200,default='')
    payer_id=models.CharField(max_length=150,default=True)
    payee_emailaddress=models.CharField(max_length=200,default='')
    currency_code=models.CharField(max_length=100,default=True)
    amount=models.CharField(max_length=150,blank=True)
    shippingaddress1=models.CharField(max_length=700,default='')
    admin_area_1=models.CharField(max_length=400,default='')
    admin_area_2=models.CharField(max_length=400,default='')
    country_code=models.CharField(max_length=400,default='')
    postal_code=models.CharField(max_length=400,default='')


# class IpModel(models.Model):
#     ip=models.CharField(max_length=100)

#     def __str__(self):
#         return self.ip


















































































































































































































































































































































































































             