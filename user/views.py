from django.shortcuts import render, HttpResponse, redirect
from home.models import extendeduser
from django.contrib.auth.models import User
from user import stats_main
from user.models import UserDetails, Channel_statistics, MostpoPularVideo




# Create your views here.


# To display Profile
def UserProfile(request):
    x= request.user
    userdetailsprofile= UserDetails.objects.get(user=x)
    extendeduser_profile= extendeduser.objects.get(user=x)
    channel_stats= Channel_statistics.objects.get(user=x)
    userprofile= User.objects.get(username=x)


    params= {'userdetails_profile':userdetailsprofile,'extendeduser_profile': extendeduser_profile, 'channel_stats': channel_stats, 'user_profile':userprofile }
    return render(request, 'user/profile.html', params)


# To add user details in the database
def Userdetails(request):
    if request.method == 'POST':
        user= request.user  

        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        phone_no= request.POST['phn_no']
        desc= request.POST['desc']
        tags= request.POST['tags']
        gender= request.POST['gender']
        image= request.POST['image']
        

        newuserdetails= UserDetails(phnno=phone_no, desc=desc, tags=tags, gender= gender, firstname=firstname, lastname=lastname, user=user, username=user)
        newuserdetails.save()


        # To save fetch stats of channel and add them ti database
        stats_main.channel_stats(user)





        return redirect('/user/profile')

