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
# All views need to be authenticated

def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("accounts:login"))
		
	# Checking for movies in user session
	if 'likedMovies' not in request.session:
		request.session['likedMovies'] = []
		request.session['dislikedMovies'] = []
		request.session['genreWeightedScore'] = {}
		return render(request, 'homepage/index.html', {
			# Setting recommended movies to false for django templating
			'recommendedMovies': False,
		})

	# Check if user list is empty
	if len(request.session['likedMovies']) == 0:
		return render(request, 'homepage/index.html', {
			# Setting recommended movies to false for django templating
			'recommendedMovies': False,
		})

	# Create list of liked genres
	likedGenres = []
	for key, value in request.session['genreWeightedScore'].items():
		if value > 0:
			likedGenres.append(key)

	# # Get movies from database where title not in dislikedMovies and not in likedMovies
	# # and genre in likedGenres, and rating is greater than 5
	# # order in descending order, and limit by 10
	# movies = models.Movie.objects.filter(
	# 	~Q(title__in=request.session['likedMovies']),
	# 	~Q(title__in=request.session['dislikedMovies']),
	# 	genre__in=likedGenres, rating__gte=5
	# ).order_by('-rating').distinct()[:6]

	# Get all movies then perform filter
	movies = models.Movie.objects.all()

	# Get rid of movies that are in likedMovies and dislikedMovies
	for movie in movies:
		if movie.title in request.session['likedMovies']:
			movies = movies.exclude(title=movie.title)
		if movie.title in request.session['dislikedMovies']:
			movies = movies.exclude(title=movie.title)

	# Get rid of movies that are not in likedGenres
	for movie in movies:
		if movie.genre not in likedGenres:
			movies = movies.exclude(title=movie.title)

	# Get rid of movies that are not greater than 5
	for movie in movies:
		if movie.rating < 5:
			movies = movies.exclude(title=movie.title)

	# get movies from movies where titles are similar to titles in likedMovies
	recommendedMovies = []

	# Make sure likedMovies has no duplicates
	likedMovies = list(set(request.session['likedMovies']))
	print(f'DEBUG INFO (SESSION) >> {request.session["likedMovies"]}')

	for movie in movies:
		for likedMovie in request.session['likedMovies']:
			# split likedMovie into array of words
			likedMovie = likedMovie.split()

			# exclude common words and articles from likedMovie title
			for word in likedMovie:
				if word.lower() in ['the', 'a', 'an', 'and', 'or', 'but', 'for', 'of', 'nor', 'on', 'to', 'with']:
					likedMovie.remove(word)

			# remove the word "the" from the movie title
			# need this bcos previous thing isn't working on the word "the"
			if 'the' in likedMovie:
				likedMovie.remove('the')
			elif 'The' in likedMovie:
				likedMovie.remove('The')

			# Remove punctuation from likedMovie title
			for word in likedMovie:
				if not word.isalpha():
					likedMovie.remove(word)


			print(f'DEBUG INFO (LIKED MOVIE) >> {likedMovie}')

			# get movies with similar titles
			for word in likedMovie:
				if word in movie.title:
					recommendedMovies.append(movie)
					break
	# Remove any duplicates from recommendedMovies
	recommendedMovies = list(dict.fromkeys(recommendedMovies))

	# Get list of genre values if the value is more than 1
	genres = []
	for key, value in request.session['genreWeightedScore'].items():
		if value > 1:
			genres.append(value)

	if len(genres) > 1:
		same = allsame(genres)

		if not same:
			# Sort ordered movies by genre
			# The greater the value a genre has in session["genres"], the higher up the movies should be in the list
			recommendedMovies = sorted(
				recommendedMovies, key=lambda x: request.session['genreWeightedScore'][x.genre], reverse=True)
		else:
			# Sort ordered movies by rating
			recommendedMovies = sorted(
				recommendedMovies, key=lambda x: x.rating, reverse=True)

	else:
		recommendedMovies = sorted(
				recommendedMovies, key=lambda x: request.session['genreWeightedScore'][x.genre], reverse=True)

	# Shortening recommended movies and re-sorting by rating
	if len(recommendedMovies) < 6:
		movies = sorted(
				movies, key=lambda x: x.rating, reverse=True)
		
		recommendedMovies = concatenate(recommendedMovies, movies)

	recommendedMovies = recommendedMovies[:6]
	recommendedMovies = sorted(
			recommendedMovies, key=lambda x: x.rating, reverse=True)

	# get liked movie objects and store in list
	likedMovies = []
	try:
		for movie in request.session['likedMovies']:
			likedMovies.append(models.Movie.objects.get(title=movie))
	except models.Movie.DoesNotExist:
		likedMovies = None

	# get disliked movie objects and store in list
	dislikedMovies = []
	try:
		for movie in request.session['dislikedMovies']:
			dislikedMovies.append(models.Movie.objects.get(title=movie))
	except models.Movie.DoesNotExist:
		dislikedMovies = None

	# Some debugging stuff
	print(request.session['likedMovies'])
	print(recommendedMovies)

	return render(request, 'homepage/index.html', {
		'recommendedMovies': recommendedMovies,
		'likedMovies': likedMovies,
		'dislikedMovies': dislikedMovies,
	})


# Helper function to see if all items in list are the same value
def allsame(array):
	same = True

	# Comparing each element with first item
	for element in array:
		if element != array[0]:
			same = False
			break

	return True if same else False

def concatenate(arr1, arr2):
	for element in arr2:
		arr1.append(element)

	return arr1
