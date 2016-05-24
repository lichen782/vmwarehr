#from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User
from django.contrib import admin
from .models import User

#user = User.objects.create
admin.site.register(User)
