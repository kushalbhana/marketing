from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, extendeduser
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib import auth




# HTML templates
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        params={}
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")

        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

    
def about(request):
    return render(request, 'home/about.html')



# Handle User Login and Signups
def HandleSignUp(request):
    return render(request, 'home/signup.html')


def HandleUserSignUp(request):
    if request.method == 'POST':
        # to create user
        if request.POST['pass1'] == request.POST['pass2']:

            # both th password matched
            # now check previous user exists
            try:
                user= User.objects.get(username=request.POST['username'])
                messages.error(request, 'The Username you entered is already taken')
                return render(request, 'home/signup.html')
            except User.DoesNotExist:
                user= User.objects.create_user(username= request.POST['username'], password= request.POST['pass1'])

                # Now to fill the data of extended feild
                chnl_name= request.POST['chanel_name']
                id_typ= request.POST['id_type']
                email= request.POST['email']
                link= request.POST['link']
                category= request.POST['category']

                newextendeduser= extendeduser(channel_name= chnl_name, channel_type= id_typ, link= link, category= category, user=user)
                newextendeduser.save()
                
                auth.login(request,user)
                return HttpResponse('Signned up !')
        else:
            messages.error(request, 'Both the Passwords you entered does not match')
            return render(request, 'home/signup.html')
    else:
        return render(request, 'register.html')

    