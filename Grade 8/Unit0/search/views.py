from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q

from homepage import models

def search(request):
    # Redirect to homepage if request method is get
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('homepage:home'))

    # Get search query from post request
    query = request.POST.get('moviename')

    # Get movies with a title that is similar to query
    movies = models.Movie.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )

    return render(request, 'search/index.html', {
        'movies': movies,
        'query': query,
    })
