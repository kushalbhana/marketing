from django.shortcuts import render, HttpResponse, redirect
from home.models import extendeduser
from django.contrib.auth.models import User
from user.models import UserDetails

# Create your views here.
def UserProfile(request):
    x= request.user
    profile= UserDetails.objects.get(user=x)
    params= {'profile':profile}
    return render(request, 'user/profile.html', params)


def Userdetails(request):
    if request.method == 'POST':
        user= request.user  
        print(user)

        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        phone_no= request.POST['phn_no']
        desc= request.POST['desc']
        tags= request.POST['tags']
        gender= request.POST['gender']
        image= request.POST['image']
        

        newuserdetails= UserDetails(phnno=phone_no, desc=desc, tags=tags, gender= gender, firstname=firstname, lastname=lastname, user=user)
        newuserdetails.save()

        return redirect('/')

