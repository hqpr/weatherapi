# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Weather, Location

admin.site.register(Weather)
admin.site.register(Location)

