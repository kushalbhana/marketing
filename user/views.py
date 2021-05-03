from django.shortcuts import render, HttpResponse
from home.models import extendeduser
from django.contrib.auth.models import User

# Create your views here.
def UserProfile(request):
    x= request.user
    profile= extendeduser.objects.get(username=x)
    params= {'profile':profile}
    return render(request, 'user/profile.html', params)
