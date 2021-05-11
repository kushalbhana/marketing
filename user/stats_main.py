from django.shortcuts import render, HttpResponse, redirect
from home.models import extendeduser
from django.contrib.auth.models import User
from user.models import UserDetails, Channel_statistics
from user.statistics import YTstats
import requests
import json




# To add statistics of channel and videos

def channel_stats(user):
    userx= extendeduser.objects.get(user=user)
    link = userx.link
    if 'https://www.youtube.com/channel/' in link:
        link= link.replace('https://www.youtube.com/channel/', '')


        
        API_KEY= 'AIzaSyB6e5pwwASwm-v6U9YdZkpdVtK1UQNKkKE'
        channel_id= link
        yt= YTstats(API_KEY, channel_id)
        data= yt.get_channel_statistics()
        
        ttl_views= data[1]['viewCount']
        print(ttl_views)
        ttl_subs= data[1]['subscriberCount']
        print(ttl_subs)
        videoCount= data[1]['videoCount']
        print(videoCount)

        channel_desc= data[0]['description']
        channel_logo= data[0]['thumbnails']['default']['url']


        total_channnel_stats= Channel_statistics(total_views=ttl_views, total_subs=ttl_subs, total_videos=videoCount, user=user, username= user, desc= channel_desc, logo=channel_logo)
        total_channnel_stats.save()

def get_all_videos(user):
    userx= extendeduser.objects.get(user=user)
    link = userx.link
    if 'https://www.youtube.com/channel/' in link:
        link= link.replace('https://www.youtube.com/channel/', '')


        API_KEY= 'AIzaSyB6e5pwwASwm-v6U9YdZkpdVtK1UQNKkKE'

        channel_id= link
        yt= YTstats(API_KEY, channel_id)
        six_videos= yt.get_channel_video_data()
        return six_videos

def youtube_thumbnail(user):
    userx= extendeduser.objects.get(user=user)
    link = userx.link
    if 'https://www.youtube.com/channel/' in link:
        link= link.replace('https://www.youtube.com/channel/', '')
        API_KEY= 'AIzaSyB6e5pwwASwm-v6U9YdZkpdVtK1UQNKkKE'
        url= f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={link}&key={API_KEY}'
        json_url= requests.get(url)
        data= json.loads(json_url.text)
        logo_data= data['items'][0]['snippet']['thumbnails']['default']['url']
        return logo_data
        

    

