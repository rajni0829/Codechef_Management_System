from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from codechef_management_app.models import Events

# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(Events)