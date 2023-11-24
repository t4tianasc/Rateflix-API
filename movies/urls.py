from django.urls import path

from .views import MovieDetailView, MoviesListView

app_name="movies"

urlpatterns = [
  path('movies/', MoviesListView.as_view()),
  path('movies/<int:movie_id>/', MovieDetailView.as_view())
]