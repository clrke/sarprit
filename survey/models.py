from django.db import models
from django.contrib.auth.models import User

class Section (models.Model):
	Course = models.CharField(max_length=10)
	Year = models.IntegerField()
	Section = models.CharField(max_length=3)


class Author (models.Model):
	Name = models.CharField(max_length=50)
	Age = models.IntegerField(max_length=5)

class Review (models.Model):
	Sentence = models.CharField(max_length=500)
	
class Sentence (models.Model):
	Words = models.CharField(max_length=30)
	