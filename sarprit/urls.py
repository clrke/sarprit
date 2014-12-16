from django.conf.urls import patterns, include, url
from django.contrib import admin

import survey.urls
import classifiers.urls
import rootword.urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^classify/', include(classifiers.urls)),
    url(r'^rootword/', include(rootword.urls)),
    url(r'', include(survey.urls)),
)
