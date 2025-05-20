from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")

def about(request):
    return HttpResponse("This is the about page")



