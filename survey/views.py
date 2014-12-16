from django.shortcuts import render, redirect
from sarprit.shortcuts import to_json
from .models import *
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from sarprit.examples import classifiers_refresh

def index(request):
	return render(request, 'survey/index.html', {"reviews": Review.objects.order_by('-id').all()})

def index2(request):
	if request.method == "POST":
		print(request.POST)
		r1 = Review(
			namedrop=request.POST['namedrop1'],
			overall_sentiment=request.POST['overall_sentiment1'],
		)
		r1.save()


		r2 = Review(
			namedrop=request.POST['namedrop2'],
			overall_sentiment=request.POST['overall_sentiment2'],
		)
		r2.save()

		if len(request.POST.getlist('sentence3[]')):
			r3 = Review(
				namedrop=request.POST['namedrop3'],
				overall_sentiment=request.POST['overall_sentiment3'],
			)
			r3.save()
		if len(request.POST.getlist('sentence4[]')):
			r4 = Review(
				namedrop=request.POST['namedrop4'],
				overall_sentiment=request.POST['overall_sentiment4'],
			)
			r4.save()


		for i in range(len(request.POST.getlist('sentence1[]'))):
			s = Sentence(
				sentence = request.POST.getlist('sentence1[]')[i],
				subjective = request.POST.getlist('subjective1[]')[i] == 'true',
				clue = request.POST.getlist('clue1[]')[i],
				rating = request.POST.getlist('rating1[]')[i],
				review = r1
			)
			s.save()


		for i in range(len(request.POST.getlist('sentence2[]'))):
			s = Sentence(
				sentence = request.POST.getlist('sentence2[]')[i],
				subjective = request.POST.getlist('subjective2[]')[i] == 'true',
				clue = request.POST.getlist('clue2[]')[i],
				rating = request.POST.getlist('rating2[]')[i],
				review = r2
			)
			s.save()

		for i in range(len(request.POST.getlist('sentence3[]'))):
			s = Sentence(
				sentence = request.POST.getlist('sentence3[]')[i],
				subjective = request.POST.getlist('subjective3[]')[i] == 'true',
				clue = request.POST.getlist('clue3[]')[i],
				rating = request.POST.getlist('rating3[]')[i],
				review = r3
			)
			s.save()

		for i in range(len(request.POST.getlist('sentence4[]'))):
			s = Sentence(
				sentence = request.POST.getlist('sentence4[]')[i],
				subjective = request.POST.getlist('subjective4[]')[i] == 'true',
				clue = request.POST.getlist('clue4[]')[i],
				rating = request.POST.getlist('rating4[]')[i],
				review = r4
			)
			s.save()

		classifiers_refresh()

		return redirect(index)
	return render(request, 'survey/index2.html', { "current_section": Section.objects.get(current = True) })

@login_required(login_url= '/admin/login/')
def sections(request):
	if request.method == 'POST':
		id = int(request.POST['id'])

		for section in Section.objects.all():
			section.current = False
			section.save()

		section = Section.objects.get(id=id)
		section.current = True
		section.save();

		return redirect(sections)

	else:
		return render(request, 'admin/sections.html', {"sections": Section.objects.all()})

@login_required(login_url='/admin/login')
def students(request):
	current_section = Section.objects.get(current=True)

	if request.method == "POST":
		data = [student.split('\t') for student in request.POST['students'].split('\r\n')]
		data = [(student[0], student[1]) for student in data]

		for student in data:
			Student(student_no=student[0], name=student[1], section=current_section).save()

		return redirect(students)

	return render(request, 'admin/students.html', { "current_section": Section.objects.get(current = True) })

@login_required(login_url= '/admin/login/')
def data(request):
	sections = []
	for section in Section.objects.all():
		section2 = model_to_dict(section)
		students = []
		sections.append(section2)
		for student in section.student_set.all():
			student2 = model_to_dict(student)
			reviews=[]
			students.append(student2)
			for review in student.review_set.all():
				review2 = model_to_dict(review)
				sentences=[]
				reviews.append(review2)
				for sentence in review.sentence_set.all():
					sentence2 = model_to_dict(sentence)
					sentences.append(sentence2)
				review2['to_str']=review.__str__()
				review2['sentences']=sentences
			student2['to_str']=student.__str__()
			student2['reviews']=reviews
		section2['to_str']=section.__str__()
		section2['students']=students

	return to_json(sections)

def data2(request):
	reviews = []
	for review in Review.objects.all():
		review2 = model_to_dict(review)
		review2['to_str'] = review.__str__()
		reviews.append(review2)

	sentences = []
	for sentence in Sentence.objects.all():
		sentence2 = model_to_dict(sentence)
		sentence2['to_str'] = sentence.__str__()
		sentences.append(sentence2)

	return to_json({"reviews":reviews, "sentences":sentences});

def reviews_table(request):
	reviews = []
	for review in Review.objects.all():
		review2 = model_to_dict(review)
		review2['to_str'] = review.__str__()
		reviews.append(review2)

	return render(request,'tables/index.html', {'reviews': reviews})
