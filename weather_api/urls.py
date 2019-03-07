from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from RestAPI.views import WeatherList, WeatherDetail, WeatherDetailErase, EraseView, WeatherTemperatureList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(regex=r'weather/$', view=WeatherList.as_view(), name='weather'),
    url(regex=r'weather/temperature/$', view=WeatherTemperatureList.as_view(), name='temperature'),
    url(regex=r'^weather/(?P<pk>[-\w]+)/$', view=WeatherDetail.as_view(), name='weather_detail'),
    url(regex=r'erase/$', view=EraseView.as_view(), name='erase'),
    url(regex=r'^erase/(?P<pk>[-\w]+)/$', view=WeatherDetailErase.as_view(), name='erase_weather'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
