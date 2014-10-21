import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

def to_json(dict):
	return HttpResponse(json.dumps(dict, cls=DjangoJSONEncoder), content_type="application/json")