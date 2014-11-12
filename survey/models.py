from django.db import models
from django.contrib.auth.models import User

class Section (models.Model):
	course = models.CharField(max_length=10)
	year = models.IntegerField()
	section = models.CharField(max_length=3)

	def __str__(self):
		return self.course.upper() + " " + str(self.year) + "-" + self.section.upper()

class Student (models.Model):
	student_no = models.IntegerField(max_length=16)
	name = models.CharField(max_length=50)
	should_display = models.BooleanField(default=false)
	section = models.ForeignKey(Section)

	def __str__(self):
		return self.name

class Review (models.Model):
	sentences = models.CharField(max_length=500)
	reviews = models.ForeignKey(Student)

	def __str__(self):
		return self.sentences
	
class Sentence (models.Model):
	sentence = models.CharField(max_length=1000)
	clue = models.CharField(max_length=1)
	review = models.CharField(max_length=30)

	def __str__(self):
		return "["+self.clue.upper()+"]" + self.sentence + self.review