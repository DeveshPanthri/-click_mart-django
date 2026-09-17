from django.contrib import admin
# from .models import User
#  use this 
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
User=get_user_model()

class UserAdmin(BaseUserAdmin):
    list_display=['email','first_name','last_name','is_active']
    fieldsets=()
     

admin.site.register(User,UserAdmin)
