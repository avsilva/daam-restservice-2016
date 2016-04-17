from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
#from django_pgjson.fields import JsonField

# Create your models here.

class Types (models.Model):
    name = models.CharField(max_length=200)

class Status (models.Model):
    name = models.CharField(max_length=200)

class Pins(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    descr = models.CharField(max_length=200, blank=True, null=True)
    type = models.ForeignKey(Types, related_name="type", default=6)
    status = models.ForeignKey(Status, related_name="status", default=1)
    comments = models.CharField(max_length=2000, blank=True, null=True)
    created = models.DateTimeField(default=datetime.now)
    assigned = models.DateTimeField(blank=True, null=True)
    resolved = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='user')
    geom = models.PointField(blank=True, null=True, srid=4326)
