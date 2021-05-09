from django.contrib import admin
from user.models import UserDetails, MostpoPularVideo, Channel_statistics

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(MostpoPularVideo)
admin.site.register(Channel_statistics)
