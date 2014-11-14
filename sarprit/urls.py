from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/sections/$', 'survey.views.sections'),
    url(r'^admin/sections/(?P<id>\d+)$', 'survey.views.set_section'),
    url(r'^admin/data/$', 'survey.views.data'),
    url(r'^$', 'survey.views.index', name='home'),
    url(r'^survey/$', 'survey.views.index2', name='home2'),
    url(r'^test/$', 'survey.views.test', name='home'),

)