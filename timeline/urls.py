from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name='timeline'

urlpatterns = [
    url(r'^$', views.timeline, name='home'),
    url(r'^share/$', views.share, name='share'),
]