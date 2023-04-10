from django.contrib.auth.models import User,auth
from django.http import HttpResponse

# def save_profile(backend, user, response, *args, **kwargs):
# def save_profile(backend, username, response, companyname, email):
    # if request.method=='POST':
    #  print("user inside SAVE PROFILEEEEE.........")   
    #  email=request.POST['email']
    #  companyname=request.POST['companyname']
    # if NewsCreator.objects.filter(user_id=user.id).count() == 0 :
    #  newsCreator = User.objects.create_user(companyname=companyname,email=email)
    #  newsCreator.save() 


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google':
        profile = user.get_socialaccount()
        if profile is None:
            profile = Socialaccount(user_id=user.id)
        profile.companyname = response.get('companyname')
        profile.email= response.get('email')
        newsCreator = User.objects.create_user(companyname=profile.companyname,email=profile.email)
        profile.save()


# def save_profile(backend, user, response, *args, **kwargs):
#     if backend.name == 'google':
#         profile = user.get_User()
#         if profile is None:
#             profile = User(user_id=user.id)
#         profile.companyname = response.get('companyname')
#         profile.email= response.get('email')
#         newsCreator = User.objects.create_user(companyname=profile.companyname,email=profile.email)
#         profile.save()                  