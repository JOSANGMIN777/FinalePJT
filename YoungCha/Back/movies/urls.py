from django.contrib import admin
from django.urls import path
from . import views
from .views import save_rating_and_comment
from .views import MovieListView
from .views import RandomMovieListView

urlpatterns = [
    # ... (이전 코드는 그대로 둠)
    path('saveRatingAndComment/<int:movie_id>/', views.save_rating_and_comment, name='save_rating_and_comment'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/random/', RandomMovieListView.as_view(), name='random-movie-list'),
    path('movieurls/', views.get_movie_datas),
]


