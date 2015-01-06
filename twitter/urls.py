from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^(?P<restaurant>[a-zA-Z\s]*)$', views.home),
)
