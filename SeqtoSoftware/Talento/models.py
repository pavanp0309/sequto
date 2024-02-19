from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model): #table name in mysql database 
    # column defination
    # columnName=datatype(required fileds)
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    mobile=models.BigIntegerField(null=False)
    # course=models.CharField(null=False)  // only for decoder website
    # subtype=models.CharField(null=False) // only for todaymonk
    message=models.CharField(null=True,max_length=100)

    class Meta:
        db_table='contacts'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
    
# job posting 
class JobPosting(models.Model):
    featured_image = models.ImageField(upload_to='images/job_images/')
    email = models.EmailField()
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_region = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    job_description = models.TextField()
    company_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    facebook_username = models.CharField(max_length=50, blank=True, null=True)
    twitter_username = models.CharField(max_length=50, blank=True, null=True)
    linkedin_username = models.CharField(max_length=50, blank=True, null=True)
    company_logo = models.ImageField(upload_to='images/company_logos/', blank=True, null=True)

    def __str__(self):
        return self.job_title