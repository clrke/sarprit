from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^1/(?P<id>\d+)/(?P<sentence>.+)', views.subjectivity),
    url(r'^2/(?P<id>\d+)/(?P<sentence>.+)', views.clues),
)
