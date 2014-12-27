from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^ka(?P<arg1>\w+)$',				views.kasarap),
	url(r'^am(?P<arg1>\w+)$',				views.amsarap),
	url(r'^ang(?P<arg1>\w+)$',				views.angsarap),
	url(r'^an(?P<arg1>\w+)$',				views.ansarap),
	url(r'^ma(?P<arg1>\w+)$',				views.masarap),
	url(r'^(?P<arg1>\w*)in(?P<arg2>\w+)$',	views.sinarap),
	url(r'^(?P<arg1>\w*)um(?P<arg2>\w+)$',	views.sumarap),
	url(r'^(?P<arg1>\w+)\1+(?P<arg2>\w+)$', views.sasarap),
)
