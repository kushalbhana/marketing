from django.shortcuts import render, HttpResponse

# Create your views here.
def ClientDashBoard(request):
    return HttpResponse('This is client')
