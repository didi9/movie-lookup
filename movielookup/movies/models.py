from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_id = models.CharField(max_length=20)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.movie_id

