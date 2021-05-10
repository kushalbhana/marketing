from django.shortcuts import render, HttpResponse, redirect
from home.models import extendeduser
from django.contrib.auth.models import User
from user.models import UserDetails, Channel_statistics
from user.statistics import YTstats




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
        ttl_views= data['viewCount']
        ttl_subs= data['subscriberCount']
        videoCount= data['videoCount']

        total_channnel_stats= Channel_statistics(total_views=ttl_views, total_subs=ttl_subs, total_videos=videoCount, user=user, username= user)
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