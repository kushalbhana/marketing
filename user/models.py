from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# For userdetails
class UserDetails(models.Model):
    username= models.CharField(max_length=20)
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    phnno= models.CharField(max_length=12, default='')
    gender= models.CharField(max_length=8)
    desc= models.TextField(max_length=500, default='')
    tags=models.CharField(max_length=50, default='')
    user= models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
         return self.username




# For statistics of the channel
class Channel_statistics(models.Model):
    username= models.CharField(max_length=20)
    total_views= models.CharField(max_length=50)
    total_subs= models.CharField(max_length=50)
    avg_views= models.CharField(max_length=50, default='')
    total_videos= models.CharField(max_length=50)
    user= models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
         return self.username



# For statistics of the most popular video 
class MostpoPularVideo(models.Model):
    username= models.CharField(max_length=20)
    title= models.CharField(max_length=100)
    desc= models.TextField(max_length=10000)
    total_views= models.CharField(max_length=50)
    total_likes= models.CharField(max_length=50)
    total_comment= models.CharField(max_length=50)
    thumbnail= models.ImageField(default=None)
    user= models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
         return self.username


