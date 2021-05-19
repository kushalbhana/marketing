from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Advertizerdetail(models.Model):
    username= models.CharField(max_length=30, primary_key=True)
    user_category= models.CharField(max_length=10)
    name= models.CharField(max_length=50)
    category= models.CharField(max_length=30)
    address= models.CharField(max_length=100)
    phno= models.CharField(max_length=12)
    city= models.CharField(max_length=20)
    state= models.CharField(max_length=30)
    zip= models.CharField(max_length=6)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    logo= models.ImageField()


    def __str__(self):
         return self.username
