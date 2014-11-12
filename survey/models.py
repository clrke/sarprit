from django.db import models
from django.contrib.auth.models import User

class Section (models.Model):
	course = models.CharField(max_length=10)
	year = models.IntegerField()
	section = models.CharField(max_length=3)
	current = models.BooleanField()

	def __str__(self):
		return self.course.upper() + " " + str(self.year) + "-" + self.section.upper()

class Student (models.Model):
	student_no = models.CharField(max_length=16)
	name = models.CharField(max_length=50)
	should_display = models.BooleanField()
	section = models.ForeignKey(Section)

	def __str__(self):
		return self.student_no.upper() + " " + self.name.upper()

class Review (models.Model):
	namedrop = models.CharField(max_length=50, blank=True)
	overall_sentiment = models.IntegerField(max_length=1)
	student = models.ForeignKey(Student)

	def __str__(self):
		review = '';
		for sentence in self.sentence_set.all():
			review += sentence.sentence;

		return review
	
class Sentence (models.Model):
	sentence = models.CharField(max_length=1000)
	subjective = models.BooleanField()
	clue = models.CharField(max_length=1)
	rating = models.IntegerField(max_length=1)
	review = models.ForeignKey(Review)

	def __str__(self):
		return "["+self.clue.upper()+"]" + self.sentence + " " + str(self.rating)