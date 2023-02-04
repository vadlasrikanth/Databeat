from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Movies(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    runtime = models.IntegerField()
    language = models.TextField()
    tagline = models.CharField(max_length=50)

class Cast(models.Model):
    mve=models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='cast',null=True,blank=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=50)
    dob = models.DateField()    

