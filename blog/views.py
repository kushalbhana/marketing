from django.shortcuts import render, HttpResponse

# Create your views here.
def BlogHome(request):
    return HttpResponse('This is blog')