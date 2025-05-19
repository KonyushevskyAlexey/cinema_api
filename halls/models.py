from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
