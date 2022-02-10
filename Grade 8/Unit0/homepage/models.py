from django.db import models

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=200)
	year = models.IntegerField()
	genre = models.CharField(max_length=200)
	director = models.CharField(max_length=200)
	stars = models.CharField(max_length=200, default="")
	rating = models.DecimalField(max_digits=3, decimal_places=1)
	image = models.CharField(max_length=1000)
	description = models.TextField()
	linkName = models.CharField(max_length=200, default="")

	def __str__(self):
		return self.title