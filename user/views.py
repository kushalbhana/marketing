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
    six_videos= stats_main.get_all_videos(x)
    first_video={}
    first_video['title']= six_videos[0][0]['title']
    first_video['publishedAt']= six_videos[0][0]['publishedAt']
    first_video['thumbnail']= six_videos[0][0]['thumbnails']['default']['url']
    first_video['stats']= six_videos[0][1]

    
    


    params= {'userdetails_profile':userdetailsprofile,'extendeduser_profile': extendeduser_profile, 'channel_stats': channel_stats, 'user_profile':userprofile, 'first_video': first_video}
    return render(request, 'user/profile.html', params)


# To add user details in the database
def Userdetails(request):
    if request.method == 'POST':
        user= request.user  

        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        phone_no= request.POST['phn_no']
        tags= request.POST['tags']
        gender= request.POST['gender']
        language= request.POST['language']
        state= request.POST['state']
        
        

        newuserdetails= UserDetails(phnno=phone_no, tags=tags, gender= gender, firstname=firstname, lastname=lastname, user=user, username=user)
        newuserdetails.save()


        # To save fetch stats of channel and add them ti database
        stats_main.channel_stats(user, language, state)
        





        return redirect('/')

