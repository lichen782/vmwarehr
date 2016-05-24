#from __future__ import unicode_literals
#from django.db import models
#from django.contrib.auth import authenticate

#class user(models.Model):
#	user = authenticate(username="User", password="pass")


from django.db import models
from django.utils import timezone

class User(models.Model):
	Username = models.CharField(max_length=200)
	Password = models.CharField(max_length=200)

#class Resume(models.Model):
