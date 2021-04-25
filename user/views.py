from django.shortcuts import render, HttpResponse

# Create your views here.
def UserProfile(request):
    return HttpResponse('This is user')
