from django.conf.urls import patterns, include, url
from django.contrib import admin

import survey.urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(survey.urls)),
)