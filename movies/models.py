from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
  return 'blog/{0}/{1}'.format(instance.title, filename)


class Movie(models.Model):
  MOVIE_GENRES = (
    ('action', 'Action'),
    ('animation', 'Animation'),
    ('comedy', 'Comedy'),
    ('documentary', 'Documentary'),
    ('drama', 'Drama'),
    ('family', 'Family'),
    ('mystery', 'Mystery'),
    ('romance', 'Romance'),
    ('science_fiction', 'Science Fiction'),
    ('thriller', 'Thriller'),
  )

  title = models.CharField(max_length=255)
  thumbnail = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
  release_date = models.DateField(default=timezone.now)
  genre = models.CharField(max_length=100, choices=MOVIE_GENRES)
  director = models.CharField(max_length=255)


class Rating(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rated_movie')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField()
  review = models.CharField(max_length=255)
  date_rated = models.DateTimeField(default=timezone.now)