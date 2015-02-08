from django.db import models
from django.contrib.auth.models import User

class Section (models.Model):
	course = models.CharField(max_length=10)
	year = models.IntegerField()
	section = models.CharField(max_length=3)
	current = models.BooleanField(default=False)

	def __str__(self):
		return self.course.upper() + " " + str(self.year) + "-" + self.section.upper()

	def review_set(self):
		return [review for student in self.student_set.all() for review in student.review_set.all()]


class Student (models.Model):
	student_no = models.CharField(max_length=16)
	name = models.CharField(max_length=50)
	should_display = models.BooleanField(default=True)
	section = models.ForeignKey(Section)

	def __str__(self):
		return self.student_no.upper() + " " + (self.name.upper() if self.should_display else "")

class Review (models.Model):
	namedrop = models.CharField(max_length=50, blank=True)
	overall_sentiment = models.IntegerField(max_length=1)
	flag = models.IntegerField(default=0)
	student = models.ForeignKey(Student, null=True, blank=True)

	def __str__(self):
		review = "["+str(self.overall_sentiment)+"] "
		for sentence in self.sentence_set.all():
			review += sentence.__str__();

		return review

	def raw_string(self):
		return ' '.join([sentence.sentence for sentence in self.sentence_set.all()])

class Sentence (models.Model):
	sentence = models.CharField(max_length=1000)
	subjective = models.BooleanField(default=True)
	clue = models.CharField(max_length=1, blank=True, null=True)
	rating = models.IntegerField(max_length=1)
	review = models.ForeignKey(Review)

	def __str__(self):
		return "["+self.clue.upper()+str(self.rating)+"] " + self.sentence + " "
