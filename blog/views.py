from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h3>Hello everybody</h3>')


def contacts(request):
    return HttpResponse('<h3>Our contacts</h3>')