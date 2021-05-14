from django.contrib import admin
from user.models import GraphAnalitycs, UserDetails, Channel_statistics

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(GraphAnalitycs)
admin.site.register(Channel_statistics)
