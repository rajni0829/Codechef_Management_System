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
    role_id = models.CharField(max_length=1,default="3")
    codechef_id = models.CharField(max_length=10,null=True,blank=True)
    event_id = models.ForeignKey(Events,on_delete=CASCADE,null=True,blank=True)



# class People(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     # admin = models.OneToOneField(CustomUser,on_delete=CASCADE)
#     event_id = models.ForeignKey(Events,on_delete=CASCADE)   
#     role_id = models.ForeignKey(settings.AUTH_USER_MODEL,
#         on_delete=CASCADE)
#     objects = models.Manager()


# class Core_Team(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     # admin = models.OneToOneField(CustomUser,on_delete=CASCADE)
#     prn_no = models.PositiveIntegerField(null=True,blank=True)
#     user_name = models.CharField(max_length=255)
#     user_email = models.CharField(max_length=255)
#     user_password = models.CharField(max_length = 255)
#     event_id = models.ForeignKey(Events,on_delete=CASCADE)   
#     objects = models.Manager()


# class Participants(models.Model):
#     full_name = models.CharField(max_length=255)
#     # admin = models.OneToOneField(CustomUser,on_delete=CASCADE)
#     codechef_id = models.AutoField(primary_key=True)
#     department = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     event_id = models.ForeignKey(Events,on_delete=CASCADE)   
#     objects = models.Manager()


# class Executive_Team(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     admin = models.OneToOneField(CustomUser,on_delete=CASCADE)
#     prn_no = models.PositiveIntegerField(null=True,blank=True)
#     user_name = models.CharField(max_length=255)
#     user_email = models.CharField(max_length=255)
#     user_password = models.CharField(max_length = 255)
#     event_id = models.ForeignKey(Events,on_delete=CASCADE)   
#     objects = models.Manager()


