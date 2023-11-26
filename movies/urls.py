from django.urls import path

from .views import MovieDetailView, MoviesListView, LatestMoviesReleasedListView

app_name="movies"

urlpatterns = [
  path('movies/', MoviesListView.as_view()),
  path('movies/<int:movie_id>/', MovieDetailView.as_view()),
  path('latest_releases/', LatestMoviesReleasedListView.as_view()),
]