from django.shortcuts import render, HttpResponse

# Create your views here.
def client(request):
    return HttpResponse('This is client')
