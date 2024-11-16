from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userinformation(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=1000,null=True,default="------")
    mail=models.CharField(max_length=1000,null=True,default="------")
    role=models.CharField(max_length=1000,null=True,default="------")
    description=models.TextField(max_length=1000,null=True,default="------")
    phone=models.CharField(max_length=20,null=True,default="------")
    github=models.CharField(max_length=600,null=True,default="------")
    hackerrank=models.CharField(max_length=600,null=True,default="------")
    portfolio=models.CharField(max_length=600,null=True,default="------")
    LeetCode=models.CharField(max_length=600,null=True,default="------")
    GFG=models.CharField(max_length=600,null=True,default="------")
    insta=models.CharField(max_length=600,null=True,default="------")
    Linkedin=models.CharField(max_length=600,null=True,default="------")
    twitter=models.CharField(max_length=600,null=True,default="------")
    facebook=models.CharField(max_length=600,null=True,default="------")
    Resume=models.CharField(max_length=600,null=True,default="------")
    codepen=models.CharField(max_length=600,null=True,default="------")
    profile_pic=models.ImageField(default='profile.jpg',null=True,blank=True)
    website=models.CharField(max_length=600,null=True,default="------")
    codechef=models.CharField(max_length=600,null=True,default="------")

    
    def __str__(self):
        return self.mail
