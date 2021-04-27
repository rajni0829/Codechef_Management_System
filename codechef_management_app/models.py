from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    start_date = models.DateTimeField(auto_now_add = True)
    end_date = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class User(AbstractUser):
    prn = models.CharField(max_length=50,null=True,blank=True)
    codechef_id = models.CharField(max_length=10,null=True,blank=True)
    event_id = models.ForeignKey(Events,on_delete=CASCADE,null=True,blank=True)
