from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:movie_name>', views.detail, name='detail'),
    # path('<str:movie_name>/<str:action>', views.detail, name='action'),
] 