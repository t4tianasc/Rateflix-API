from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


class MoviesListView(APIView):
  def get(self, request, *args, **kwargs):
    movies = Movie.objects.all()
    serializer = Movie(movies, many=True)

    return Response(serializer.data)
  
