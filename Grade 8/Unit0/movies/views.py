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

    return render(request, 'index.html', {
        'movieMatrix': movie_matrix,
    })

def detail(request, movie_name):
    movie = models.Movie.objects.get(linkName=movie_name)

    # check if movie is empty
    if movie is None:
        return render(request, 'detail.html', {
            'movie': None,
        })
    
    return render(request, 'detail.html', {
        'movie': movie,
    })