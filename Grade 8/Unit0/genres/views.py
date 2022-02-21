from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q

from homepage import models

# Create your views here.
def action(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("accounts:login"))
		
	# Get list of all movies with "Action" genre
	movies = models.Movie.objects.filter(genre="Action")
	return render(request, 'genres/index.html', {
		'action': movies,
	})

def comedy(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("accounts:login"))
		
	# Get list of all movies with "Comedy" genre
	movies = models.Movie.objects.filter(genre="Comedy")
	return render(request, 'genres/index.html', {
		'comedy': movies,
	})

def horror(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("accounts:login"))
		
	# Get list of all movies with "Horror" genre
	movies = models.Movie.objects.filter(genre="Horror")
	return render(request, 'genres/index.html', {
		'horror': movies,
	})

def fantasy(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("accounts:login"))
		
	# Get list of all movies with "Fantasy" genre
	movies = models.Movie.objects.filter(genre="Fantasy")
	return render(request, 'genres/index.html', {
		'fantasy': movies,
	})