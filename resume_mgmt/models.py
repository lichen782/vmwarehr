from __future__ import unicode_literals
from django.db import models


class Resume(models.Model):
    genderchoices = (('M', 'Male'), ('F', 'Female'))
    statuschoices = (('Received', 'Received'),
                     ('Pending', 'Pending'),
                     ('Interviewed', 'Interviewed'),
                     ('Accepted', 'Accepted'),
                     ('Rejected', 'Rejected'),)
    applicationtype = (('Internship', 'Internship'), ('Full Time Employee', 'Full Time Employee'))

    name = models.CharField(max_length=200, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    age = models.IntegerField(null=True, blank=False)
    telephone = models.IntegerField(null=True, blank=False)
    address = models.CharField(max_length=350, null=True, blank=False)
    gender = models.CharField(max_length=1, choices=genderchoices, null=True, blank=False)
    grad_year = models.IntegerField(null=True, blank=False)
    school = models.CharField(max_length=350, null=True, blank=False)
    create_date = models.DateField(null=True, blank=False)
    status = models.CharField(max_length=25, null=False, blank=False, choices=statuschoices, default='Received')
    Application_Type = models.CharField(max_length=30, choices=applicationtype, null=True, blank=False)

    def save(self, *args, **kwargs):
        self.name = self.name[0].upper() + self.name[1:].lower()
        super(Resume, self).save(*args, **kwargs)
