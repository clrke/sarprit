from django.conf.urls import patterns, include, url
from django.contrib import admin

import survey.urls
import classifiers.urls
import rootword.urls
import twitter.urls

def review_save(request, id, flag):
	from survey.models import Review
	from django.http import JsonResponse

	review = Review.objects.get(id=int(id))
	review.flag = int(flag)
	review.save()
	return JsonResponse({'id':id})

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^classify/', include(classifiers.urls)),
    url(r'^reviews/$', "survey.views.reviews_table"),
    url(r'^reviews\.json$', "survey.views.reviews_json"),
    url(r'^reviews/add', "survey.views.reviews_add"),
    url(r'^rootword/', include(rootword.urls)),
    url(r'', include(survey.urls)),
    url(r'^twitter/', include(twitter.urls)),
    url(r'^review/save/(?P<id>\d+)/(?P<flag>\d)', review_save)
)
