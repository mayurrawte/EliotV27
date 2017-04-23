from __future__ import unicode_literals

from django.db import models

# Create your models here.


class StaffUser(models.Model):
    name = models.CharField(max_length=200),
    email = models.EmailField()
    password = models.CharField(max_length=200)

