from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()
    genres = models.ManyToManyField(Genre)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    rating = models.FloatField()

    def __str__(self):
        return self.title
