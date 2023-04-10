# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import *

# class PostedJobAdmin(admin.ModelAdmin):
#     list_display = ('jobtitle', 'companyname','email')

class JobsekerProfileAdmin(admin.ModelAdmin):
    list_display = ('fullname','email','address') 

class AppliedJobsAdmin(admin.ModelAdmin):
    list_display = ('jobtitle','currentjob','companyname')

class UserAdmin(admin.ModelAdmin): 
    list_display = ('username','email','last_login')   

class EmployeeContactAdmin(admin.ModelAdmin):
     list_display =('Fullname','email','companyname')

class ContactDetailAdmin(admin.ModelAdmin):
     list_display =('contactname','contactemail')




# admin.site.register(PostedJob,PostedJobAdmin)
admin.site.register(PostedJob)
admin.site.register(JobsekerProfile,JobsekerProfileAdmin)
admin.site.register(AppliedJobs,AppliedJobsAdmin)
admin.site.register(EmployerContact,EmployeeContactAdmin)
admin.site.register(ContactDetail,ContactDetailAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Skills)
admin.site.register(Payment_Details)
# admin.site.register(IpModel)