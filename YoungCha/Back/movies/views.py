from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .serializers import *
from django.db.models import Count
import random
import requests
from django.conf import settings

api_key = settings.API_KEY


@api_view(['GET'])
def get_genre_datas(request):
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=ko-KR'
    response = requests.get(url).json()

    for genre in response['genres']:
        save_data = {
            'name': genre.get('name')
        }
        serializers = GenreSerializer(data=save_data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(id=genre['id'])
    return Response(response)



@api_view(['GET'])
def get_movie_datas(request):

    for i in range(1, 101):
        url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=ko-KR&page={i}'  
        response = requests.get(url).json()

        movie_list = response.get('results')
        for movie in movie_list:
            if movie.get('release_date', '') and (movie.get('overview') != '' and movie.get('poster_path') != None and movie.get('release_date') != None):
                fields = {
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'overview': movie['overview'],
                    'vote_average': movie['vote_average'],
                    'vote_count' : movie['vote_count'],
                    'poster_path': movie['poster_path'],
                    
                    # 'video': [],
                    'like_users' : [],            
                }
                serializer = MovieSaveSerializer(data=fields)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(user=request.user, id=movie['id'])
                genres = movie.get('genre_ids')
                movie = Movie.objects.get(pk=movie['id'])
                for genre in genres:
                    movie.genre_check.add(genre)


                

    return Response(response)


@api_view(['POST'])
def movie_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)


    if request.method == 'POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)

        else:
            movie.like_users.add(request.user)
    

    return Response(serializer.data)