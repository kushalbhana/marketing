from django.shortcuts import render, HttpResponse
from .models import Contact

# HTML templates
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            return render(request,'home/contact.html')
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
    return render(request, "home/contact.html")
    

def about(request):
    return render(request, 'home/about.html')
