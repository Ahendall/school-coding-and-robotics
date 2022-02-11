from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from homepage import models

# Create your views here.


def index(request):
	movies = models.Movie.objects.all()

	# sort movies in alphabetical order
	movies = sorted(movies, key=lambda x: x.title)


	return render(request, 'movies/index.html', {
		'movies': movies,
	})

# Movie detail rendering stuff


def detail(request, movie_name):
	# Exception handle in case no movie is returned
	try:
		movie = models.Movie.objects.get(linkName=movie_name)
		print(movie)
		if movie.title in request.session['likedMovies']:
			if movie.title == "Shrek":
				return render(request, 'movies/detail.html', {
					'movie': movie,
					'liked': True,
					'shrek': True,
				})
			return render(request, 'movies/detail.html', {
				'movie': movie,
				'liked': True,
			})

		elif movie.title in request.session['dislikedMovies']:
			if movie.title == "Shrek":
				return render(request, 'movies/detail.html', {
					'movie': movie,
					'disliked': True,
					'shrek': True,
				})
			return render(request, 'movies/detail.html', {
				'movie': movie,
				'disliked': True,
			})

		else:
			if movie.title == "Shrek":
				return render(request, 'movies/detail.html', {
					'movie': movie,
					'shrek': True,
				})
			return render(request, 'movies/detail.html', {
				'movie': movie,
			})
	except:
		return render(request, 'movies/detail.html', {
			'movie': None,
		})


def like(request, movie_name):
	# get movie
	try:
		movie = models.Movie.objects.get(linkName=movie_name)
	except:
		# redirect to main movie page
		return HttpResponseRedirect(reverse('movies:index'))

	# update session likedMovies
	if 'likedMovies' not in request.session:
		request.session['likedMovies'] = []

	if movie.title not in request.session['likedMovies']:
		request.session['likedMovies'].append(movie.title)

	# remove movie if it is in dislike list
	if movie.title in request.session['dislikedMovies']:
		request.session['dislikedMovies'].remove(movie.title)

	# update session genreWeightedScore
	if 'genreWeightedScore' not in request.session:
		request.session['genreWeightedScore'] = {}

	if movie.genre not in request.session['genreWeightedScore']:
		request.session['genreWeightedScore'][movie.genre] = 1
	else:
		request.session['genreWeightedScore'][movie.genre] += 1

	# redirect to movie detail page
	return HttpResponseRedirect(reverse('movies:detail', args=(movie.linkName,)))


def dislike(request, movie_name):
	# get movie
	try:
		movie = models.Movie.objects.get(linkName=movie_name)
	except:
		# redirect to main movie page
		return HttpResponseRedirect(reverse('movies:index'))

	# update session dislikedMovies
	if 'dislikedMovies' not in request.session:
		request.session['dislikedMovies'] = []

	if movie.title not in request.session['dislikedMovies']:
		request.session['dislikedMovies'].append(movie.title)

	# remove movie if it is in liked list
	if movie.title in request.session['likedMovies']:
		request.session['likedMovies'].remove(movie.title)

	# update session genreWeightedScore
	if 'genreWeightedScore' not in request.session:
		request.session['genreWeightedScore'] = {}

	if movie.genre not in request.session['genreWeightedScore']:
		request.session['genreWeightedScore'][movie.genre] = -1
	else:
		request.session['genreWeightedScore'][movie.genre] -= 1

	# redirect to movie detail page
	return HttpResponseRedirect(reverse('movies:detail', args=(movie.linkName,)))
