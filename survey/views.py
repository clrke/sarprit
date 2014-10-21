from django.shortcuts import render
from sarprit.shortcuts import to_json
from sklearn.svm import SVC

def index(request):
	return render(request, 'survey/index.html')

def test(request):
	return to_json({"message": "Hello", "target": "World"})
