__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django.conf import settings
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class EventHost(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return '%s: Host of %s' % (self.user.get_full_name(), self.event)


class EventGuest(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return '%s: Guest at %s' % (self.user.get_full_name(), self.event)


class Product(models.Model):
    name = models.CharField(max_length=250)
    style = models.CharField(max_length=250)
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    producer = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name


class EventProduct(models.Model):
    event = models.ForeignKey(Event)
    product = models.ForeignKey(Product)
    order = models.IntegerField()

    def __unicode__(self):
        return '%s in %s' % (self.product, self.event)


class Response(models.Model):
    best_product = models.ForeignKey(EventProduct)
    product_list = models.CommaSeparatedIntegerField()


class EventGuestResponse(models.Model):
    event_guest = models.ForeignKey(EventGuest)
    response = models.ForeignKey(Response)