
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

# This is where all the data
def detail(request, movie_name, action=None):
    # Exception handle in case no movie is returned
    try:
        movie = models.Movie.objects.get(linkName=movie_name)
    except:
        return render(request, 'movies/detail.html', {
            'movie': None,
        })

    # Check if user has liked or disliked the movie
    if action == 'like' and movie.title not in request.session['likedMovies'] and request.method == 'POST':
        request.session['likedMovies'].append(movie.title)

        # remove movie from disliked list if it is there
        if movie.title in request.session['dislikedMovies']:
            request.session['dislikedMovies'].remove(movie.title)

        # Update genreWeightedScore
        for genre in movie.genre.split(','):
            if genre in request.session['genreWeightedScore']:
                request.session['genreWeightedScore'][genre] += 1
            else:
                request.session['genreWeightedScore'][genre] = 1

        return render(request, 'movies/detail.html', {
            'movie': movie,
            'like': True
        })

    elif action == 'dislike' and movie.title not in request.session['dislikedMovies'] and request.method == 'POST':
        request.session['dislikedMovies'].append(movie.title)

        # Remove movie from liked movies if it is there
        if movie.title in request.session['likedMovies']:
            request.session['likedMovies'].remove(movie.title)

        # Update genreWeightedScore
        for genre in movie.genre.split(','):
            if genre in request.session['genreWeightedScore']:
                request.session['genreWeightedScore'][genre] -= 1
            else:
                request.session['genreWeightedScore'][genre] = -1

        return render(request, 'movies/detail.html', {
            'movie': movie,
            'dislike': True,
        })

    return render(request, 'movies/detail.html', {
        'movie': movie,
    })
