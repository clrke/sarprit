from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^1/(?P<sentence>.+)/(?P<id>\d+)', views.subjectivity),
)
