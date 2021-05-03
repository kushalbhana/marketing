from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, extendeduser
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout




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
                user= User.objects.create_user(username= request.POST['username'], password= request.POST['pass1'], email= request.POST['email'])

                # Now to fill the data of extended feild
                username= request.POST['username']
                chnl_name= request.POST['chanel_name']
                id_typ= request.POST['id_type']
                email= request.POST['email']
                link= request.POST['link']
                category= request.POST['category']

                newextendeduser= extendeduser( username= username ,channel_name= chnl_name, channel_type= id_typ, link= link, category= category, user=user)
                newextendeduser.save()
                
                context= {'newextendeduser': newextendeduser}
                auth.login(request,user)
                messages.success(request, 'Account Successfully Created')
                return render(request, 'home/userdetails.html', context)

        else:
            messages.error(request, 'Both the Passwords you entered does not match')
            return render(request, 'home/signup.html')
    else:
        return render(request, 'register.html')

def userdetails(request):
    if request.method == 'POST':
        user= request.user  

        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        phone_no= request.POST['phn_no']
        desc= request.POST['desc']
        tags= request.POST['tags']
        gender= request.POST['gender']
        image= request.POST['image']

        User.objects.update(first_name=firstname, last_name=lastname)
        extendeduser.objects.update(phnno=phone_no, desc=desc, tags=tags, gender= gender, channel_logo= image)

        return redirect('/')

def handleLogin(request):
        if request.method=="POST":
            # Get the post parameters
            loginusername=request.POST['username']
            loginpassword=request.POST['password']
            user= authenticate(username= loginusername, password= loginpassword)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged In')
                return redirect('/')

            else:
                messages.error(request, 'Invalid Username or Password, Please try again')
                return redirect('/')
        return HttpResponse("404 - Not found")


def handleLogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect(home)
        

    