from django.db import models
from django.contrib.auth.models import User

class Section (models.Model):
	course = models.CharField(max_length=10)
	year = models.IntegerField()
	section = models.CharField(max_length=3)