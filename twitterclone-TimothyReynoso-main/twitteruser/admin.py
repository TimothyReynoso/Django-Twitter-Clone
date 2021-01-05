from django.contrib import admin

# Register your models here.
from twitteruser.models import MyUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(MyUser, UserAdmin)