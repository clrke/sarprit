from django.shortcuts import render
from django.http import HttpResponse

def sinarap	(request, arg1, arg2):	return HttpResponse(arg1 + arg2)
def masarap	(request, arg1):		return HttpResponse(arg1)
def kasarap	(request, arg1):		return HttpResponse(arg1)
def angsarap(request, arg1):		return HttpResponse(arg1)
def sumarap	(request, arg1, arg2):	return HttpResponse(arg1 + arg2)
def sasarap	(request, arg1, arg2):	return HttpResponse(arg1 + arg2)
def amsarap	(request, arg1):		return HttpResponse(arg1)
def ansarap (request, arg1):		return HttpResponse(arg1)
