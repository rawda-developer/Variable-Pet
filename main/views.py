from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Home</h1>')


def pet_details(request, pk=1):
    return HttpResponse('<h1>Pet Detail</h1>')
