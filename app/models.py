__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=250)

    def __unicode__(self):
        return self.title