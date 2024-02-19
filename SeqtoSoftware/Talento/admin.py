from django.contrib import admin
# importing the databases tabales
from . models import Contact ,JobPosting,Profile

# 
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile')

# Register your models here.
admin.site.register(Contact)
admin.site.register(JobPosting)
admin.site.register(Profile)

