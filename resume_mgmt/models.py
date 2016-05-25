#from __future__ import unicode_literals
#from django.db import models
#from django.contrib.auth import authenticate

#class user(models.Model):
#	user = authenticate(username="User", password="pass")


from django.db import models
from django import forms

class User(models.Model):
	name = forms.CharField(max_length=200)
	email = forms.EmailField()
	age = forms.IntegerField()
	telephone = forms.IntegerField()
	address = forms.CharField()
	gender = forms.ChoiceField()


#class Resume(models.Model):
