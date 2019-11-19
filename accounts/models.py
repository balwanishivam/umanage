from django.db import models
from django.contrib.auth.models import User

from user.models import *
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username
#class UserProfileInfo(models.Model):
#    user = models.OneToOneField(User,on_delete=models.CASCADE)
#    portfolio_site = models.URLField(blank=True)
#    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
#    def __str__(self):
#        return self.user.username
#from django.db import models
#from user.models import * 
#class register(details):
#    username=models.CharField(max_length=200 )
#    password=models.CharField(max_length=100,primary_key=True)
#    security_question=models.CharField(max_length=500)
#    security_answer=models.CharField(max_length=500)

    

# Create your models here.
