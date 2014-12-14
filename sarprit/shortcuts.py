import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

def to_json(dict):
	return HttpResponse(json.dumps(dict, cls=DjangoJSONEncoder), content_type="application/json")

def normalize_sentiment(rating):
	if rating > 3:
		return 2
	elif rating < 3:
		return 0
	else:
		return 1
