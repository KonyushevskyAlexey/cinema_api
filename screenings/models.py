from django.db import models
from movies.models import Movie
from halls.models import Hall

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.movie.title} at {self.start_time}"

    def save(self, *args, **kwargs):
        # Автоматически вычисляем end_time на основе продолжительности фильма
        if not self.end_time and self.movie:
            self.end_time = self.start_time + self.movie.duration
        super().save(*args, **kwargs)
