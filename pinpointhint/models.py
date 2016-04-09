from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
#from django_pgjson.fields import JsonField

# Create your models here.

class Pins(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    descr = models.CharField(max_length=200, blank=True, null=True)
    geom = models.PointField(blank=True, null=True, srid=4326)
