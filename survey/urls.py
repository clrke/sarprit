from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^admin/sections/$', views.sections),
    url(r'^admin/students/$', views.students),
    url(r'^admin/data/$', views.data),

    url(r'^api/data/$', views.data2),

    url(r'^$', views.index, name='home'),
    url(r'^survey/$', views.index2, name='home2'),

    url(r'^sentence/preprocess/(?P<review>.+)$', views.preprocess),
    url(r'^sentence/classify/(?P<id>\d+)/(?P<sentence>.+)$', views.classify),
    url(r'^review/classify/(?P<f>\d+)/(?P<h>\d+)/(?P<m>\d+)/(?P<g>\d+)$',
    	views.classify_overall_sentiment),
)
