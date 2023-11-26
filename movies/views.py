from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


class MoviesListView(APIView):
  def get(self, request, *args, **kwargs):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)
  

class MovieDetailView(APIView):
  def get(self, request, movie_id, *args, **kwargs):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(movie)

    return Response(serializer.data)


class LatestMoviesReleasedListView(APIView):
  def get(self, request, *args, **kwargs):
    limit_str = request.GET.get('limit', '15')
    limit = int(limit_str)
    max_limit = 20
    if limit > max_limit:
      return HttpResponse(f"Invalid limit value, max allowed: {max_limit}", status=400)

    movies = Movie.objects.all().order_by('-release_date')[:limit]
    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)
