# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from jsonfield import JSONField


class Weather(models.Model):
    date = models.DateField()
    location = models.ForeignKey('Location')

    def __unicode__(self):
        return "%s" % self.date

    class Meta:
        ordering = ['-id', ]

    @property
    def get_lowest_temperature(self):
        return min(list(self.location.temperature))

    @property
    def get_highest_temperature(self):
        return max(list(self.location.temperature))


class Location(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    temperature = JSONField(blank=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.city, self.state)


