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
        print(link)

        API_KEY= 'AIzaSyB9h8mAYG-DHmExLfu7AFMjS9P0ApBCBlY'
        channel_id= link
        yt= YTstats(API_KEY, channel_id)
        data= yt.get_channel_statistics()
        ttl_views= data['viewCount']
        ttl_subs= data['subscriberCount']
        videoCount= data['videoCount']

        total_channnel_stats= Channel_statistics(total_views=ttl_views, total_subs=ttl_subs, total_videos=videoCount, user=user, username= user)
        total_channnel_stats.save()
