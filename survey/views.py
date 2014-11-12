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
		return to_json(request.POST)
	return render(request, 'survey/index2.html')

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

