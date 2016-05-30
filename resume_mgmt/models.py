from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import authenticate
from django.db import models
from django import forms

#class user(models.Model):
	#user = authenticate(username="User", password="pass")

class Resume(models.Model):
	genderchoices = (('M', 'Male'), ('F', 'Female'))

	name = models.CharField(max_length=200, null=True, blank=False)
	email = models.EmailField(null=True, blank=False)
	age = models.IntegerField(null=True, blank=False)
	telephone = models.IntegerField(null=True, blank=False)
	address = models.CharField(max_length=350, null=True, blank=False)
	gender = models.CharField(max_length=1, choices=genderchoices, null=True, blank=False)
	school = models.CharField(max_length=350, null=True, blank=False)
	start_date = models.DateField(null=True, blank=False)
	end_date = models.DateField(null=True, blank=False)


	def __unicode__(self):
		return self.email


#class Resume(models.Model):
