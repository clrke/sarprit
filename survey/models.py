from django.db import models
from django.contrib.auth.models import User

class Section (models.Model):
	course = models.CharField(max_length=10)
	year = models.IntegerField()
	section = models.CharField(max_length=3)


class Student (models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField(max_length=5)

class Review (models.Model):
	sentences = models.CharField(max_length=500)
	
class Sentence (models.Model):
	sentence = models.CharField(max_length=1000)
	clue = models.CharField(max_length=50)
	review = models.CharField(max_length=30)
	