from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q

from . import models

# Create your views here.


def index(request):
    # Checking for movies in user session
    if 'likedMovies' not in request.session:
        request.session['likedMovies'] = []
        request.session['dislikedMovies'] = []
        request.session['genreWeightedScore'] = {}
        return render(request, 'index.html', {
            # Setting recommended movies to false for django templating
            'recommendedMovies': False,
        })

    # Check if user list is empty
    if len(request.session['likedMovies']) == 0:
        return render(request, 'index.html', {
            # Setting recommended movies to false for django templating
            'recommendedMovies': False,
        })

    # Create list of liked genres
    likedGenres = []
    for key, value in request.session['genreWeightedScore'].items():
        if value > 0:
            likedGenres.append(key)

    # Get movies from database where title not in dislikedMovies and not in likedMovies
    # and genre in likedGenres, and rating is greater than 5
    # order in descending order, and limit by 20
    movies = models.Movie.objects.filter(
        ~Q(title__in=request.session['likedMovies']),
        ~Q(title__in=request.session['dislikedMovies']),
        genre__in=likedGenres, rating__gte=5
    ).order_by('-rating').distinct()[:20]

    return render(request, 'index.html', {
        'recommendedMovies': movies,
    })