from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^admin/sections/$', views.sections),
    url(r'^admin/students/$', views.students),
    url(r'^admin/sections/(?P<id>\d+)$', views.set_section),
    url(r'^admin/data/$', views.data),

    url(r'^$', views.index, name='home'),
    url(r'^survey/$', views.index2, name='home2'),
)
