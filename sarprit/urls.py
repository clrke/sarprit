from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'survey.views.index', name='home'),
    url(r'2/', 'survey.views.index2', name='home2'),
    url(r'test/', 'survey.views.test', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
