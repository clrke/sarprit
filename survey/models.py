from django.db import models
from django.contrib.auth.models import User

class Section (models.Model):
	course = models.Charfield(max_length=4)
	year = models.Integerfield()
	section = models.Integerfield()