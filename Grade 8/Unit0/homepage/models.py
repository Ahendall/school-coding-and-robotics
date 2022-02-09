from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    genre = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    rating = models.IntegerField()
    image = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title