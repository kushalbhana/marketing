from django.shortcuts import render, HttpResponse, redirect
from home.models import extendeduser
from django.contrib.auth.models import User
from user.models import UserDetails, Channel_statistics
from user.statistics import YTstats
import requests
import json




# To add statistics of channel and videos

def channel_stats(user, language, state):
    userx= extendeduser.objects.get(user=user)
    link = userx.link
    if 'https://www.youtube.com/channel/' in link:
        link= link.replace('https://www.youtube.com/channel/', '')


        
        API_KEY= 'AIzaSyB9h8mAYG-DHmExLfu7AFMjS9P0ApBCBlY'
        channel_id= link
        yt= YTstats(API_KEY, channel_id)
        data= yt.get_channel_statistics()
        
        
        ttl_views= data[1]['viewCount']
        ttl_subs= data[1]['subscriberCount']
        videoCount= data[1]['videoCount']
        
        channel_desc= data[0]['description']
        channel_name= data[0]['title']
        country= data[0]['country']
        channel_logo= data[0]['thumbnails']['medium']['url']
        content_language= language


        total_channnel_stats= Channel_statistics(total_views=ttl_views, total_subs=ttl_subs, total_videos=videoCount, user=user, username= user, desc= channel_desc, logo=channel_logo, country=country, language=content_language, channel_name=channel_name, state= state)
        total_channnel_stats.save()

def get_all_videos(user):
    userx= extendeduser.objects.get(user=user)
    link = userx.link
    if 'https://www.youtube.com/channel/' in link:
        link= link.replace('https://www.youtube.com/channel/', '')


        API_KEY= 'AIzaSyB9h8mAYG-DHmExLfu7AFMjS9P0ApBCBlY'

        channel_id= link
        yt= YTstats(API_KEY, channel_id)
        six_videos= yt.get_channel_video_data()
        return six_videos


        

    

