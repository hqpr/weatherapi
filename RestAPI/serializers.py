from rest_framework.fields import ReadOnlyField

from .models import Weather, Location
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('lat', 'lon', 'city', 'state', 'temperature')


class WeatherSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Weather
        fields = ('date', 'location')
        depth = 1

    def create(self, validated_data):
        location_data = validated_data.get('location')
        location = Location.objects.create(**location_data)
        instance = Weather.objects.create(**validated_data)
        instance.location = location
        instance.save()
        return super(WeatherSerializer, self).create(validated_data)


class TemperatureSerializer(serializers.ModelSerializer):
    lat = serializers.CharField(source='location.lat')
    lon = serializers.CharField(source='location.lon')
    city = serializers.CharField(source='location.city')
    state = serializers.CharField(source='location.state')
    lowest = ReadOnlyField(source='get_lowest_temperature')
    highest = ReadOnlyField(source='get_highest_temperature')

    class Meta:
        depth = 1
        model = Weather
        fields = ('lat', 'lon', 'city', 'state', 'lowest', 'highest')




