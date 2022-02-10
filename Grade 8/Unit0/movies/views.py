
from django.shortcuts import render
from homepage import models

# Create your views here.
def index(request):
    # convert movies into a matrix
    movies = models.Movie.objects.all()

    # sort movies in alphabetical order
    movies = sorted(movies, key=lambda x: x.title)

    movie_matrix = []
    while movies:
        movie_matrix.append(list(movies[:5]))
        movies = movies[5:]

    return render(request, 'movies/index.html', {
        'movieMatrix': movie_matrix,
    })

def detail(request, movie_name):
	try:
    	movie = models.Movie.objects.get(linkName=movie_name)
	except:
		return render(request, 'movies/detail.html', {
            'movie': None,
        })

    # check if movie is empty
    
    return render(request, 'movies/detail.html', {
        'movie': movie,
    })