# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Weather, Location
from .serializers import WeatherSerializer, TemperatureSerializer
from django_filters.rest_framework import DjangoFilterBackend


class WeatherList(generics.ListCreateAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        lat = self.request.query_params.get('lat')
        lon = self.request.query_params.get('lon')
        if all([lat, lon]):
            return Weather.objects.filter(location__lat__exact=lat, location__lon__exact=lon)
        return super(WeatherList, self).get_queryset()


class WeatherTemperatureList(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = TemperatureSerializer

    def get_queryset(self):
        queryset = super(WeatherTemperatureList, self).get_queryset()
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        if all([start, end]):
            queryset = Weather.objects.filter(date__gte=start, date__lte=end)
        return queryset


class WeatherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    http_method_names = ['get', 'post', 'head', 'put']


class WeatherDetailErase(WeatherDetail):
    http_method_names = ['delete', ]


class EraseView(APIView):
    def post(self, request, *args, **kwargs):
        return Weather.objects.all().delete()
