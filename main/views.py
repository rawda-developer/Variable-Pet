from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Pet, Vaccine


class Home(ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'main/home.html'


class PetDetails(DetailView):
    model = Pet
    context_object_name = 'pet'
    template_name = 'main/pet_details.html'
