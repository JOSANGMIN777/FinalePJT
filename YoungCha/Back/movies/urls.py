from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # ... (이전 코드는 그대로 둠)
    # path('saveRatingAndComment/<int:movie_id>/', views.save_rating_and_comment, name='save_rating_and_comment'),
    # path('movies/', MovieListView.as_view(), name='movie-list'),
    # path('movies/random/', RandomMovieListView.as_view(), name='random-movie-list'),
    path('moviegenres/', views.get_genre_datas),
    path('movieurls/', views.get_movie_datas),

    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/like/', views.movie_like),
    
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/like/', views.comment_like),
    path('community/<int:movie_pk>/create/', views.comment_create),
]   


