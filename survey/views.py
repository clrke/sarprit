from django.shortcuts import render
from sarprit.shortcuts import to_json

def index(request):
	person = {
		"name" : "Regine", 
		"age" : 19
	}
	return render(request, 'survey/index.html', {"person": person})

def index2(request):
	if request.method == "POST":
		return to_json(request.POST)
	return render(request, 'survey/index2.html')

def test(request):
	return to_json([{"data1": "Hello", "data2": "World"}, {"data1": "I", "data2": "am"}, {"data1": "Clarke", "data2": "Plumo"}])
