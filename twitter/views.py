from django.shortcuts import render
from . import api

def home(request, restaurant):
	reviews = api.search(restaurant)
	print(reviews)
	return render(request, 'twitter/index.html', {'reviews': reviews, 'restaurant': restaurant})
