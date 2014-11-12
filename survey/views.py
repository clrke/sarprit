from django.shortcuts import render, redirect
from sarprit.shortcuts import to_json
from .models import *
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


def index(request):
	person = {
		"name" : "Regine", 
		"age" : 19
	}
	return render(request, 'survey/index.html', {"person": person})

def index2(request):
	if request.method == "POST":
		r1 = Review(
			namedrop=request.POST['namedrop1'],
			overall_sentiment=request.POST['overall_sentiment1'],
			student=Student.objects.filter(student_no__iexact=request.POST['student'])[0]
		)
		r1.save()

		r2 = Review(
			namedrop=request.POST['namedrop2'],
			overall_sentiment=request.POST['overall_sentiment2'],
			student=Student.objects.filter(student_no__iexact=request.POST['student'])[0]
		)
		r2.save()

		if request.POST['overall_sentiment3']:
			r3 = Review(
				namedrop=request.POST['namedrop3'],
				overall_sentiment=request.POST['overall_sentiment3'],
				student=Student.objects.filter(student_no__iexact=request.POST['student'])[0]
			)
			r3.save()
		if request.POST['overall_sentiment4']:
			r4 = Review(
				namedrop=request.POST['namedrop4'],
				overall_sentiment=request.POST['overall_sentiment4'],
				student=Student.objects.filter(student_no__iexact=request.POST['student'])[0]
			)
			r4.save()

		return to_json(request.POST)
	return render(request, 'survey/index2.html', { "current_section": Section.objects.get(current = True) })

def test(request):
	return to_json([{"data1": "Hello", "data2": "World"}, {"data1": "I", "data2": "am"}, {"data1": "Clarke", "data2": "Plumo"}])

@login_required(login_url= '/admin/login/')
def sections(request):
	sections = Section.objects.all()
	return render(request, 'admin/sections.html', {"sections": sections})

@login_required(login_url= '/admin/login/')
def set_section(request,id):
	for section in Section.objects.all():
		section.current = False
		section.save()

	section = Section.objects.get(id=id)
	section.current = True
	section.save();

	return redirect(sections)


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
				review2['sentences']=sentences
			student2['reviews']=reviews
		section2['students']=students

	return to_json(sections)

