from django.urls import path
from . import views

app_name = 'genres'
urlpatterns = [
    path('action/', views.action, name='action'),
    path('comedy/', views.comedy, name='comedy'),
    path('horror/', views.horror, name='horror'),
    path('fantasy/', views.fantasy, name='fantasy'),
]
