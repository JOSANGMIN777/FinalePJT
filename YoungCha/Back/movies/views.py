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


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def save_rating_and_comment(request, movie_id):
#     if request.method == "POST":
#         movie = get_object_or_404(Movies, pk=movie_id)
#         serializer = MovieCommentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             # serializer.save()
#             serializer.save(movie=movie, user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.data, status=201)  # 새로운 코멘트를 생성한 경우 201 Created 반환
#     else:
#         return JsonResponse({"message": "잘못된 요청입니다."}, status=400)
    
# class MovieListView(ListAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MovieListSerializer

# class RandomMovieListView(ListAPIView):
#     serializer_class = MovieListSerializer

#     def get_queryset(self):
#         # 랜덤으로 5개의 영화 선택
#         return random.sample(list(Movies.objects.all()), min(5, Movies.objects.count()))
    

@api_view(['GET'])
def get_movie_datas(request):

    # total_data = []

    # genres_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=ko-KR'
    # genres = request.get(genres_url).json()
    
    # genre_list = genres.get('genres')

    # for genre in genre_list:
    #     fields = {
    #         'name': genre['name'],
    #     }

    #     data = {
    #         "model": "movies.genre",
    #         "pk": genre['id'],
    #         "fields": fields,
    #     }

    #     total_data.append(data)

    for i in range(1, 3):
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
                    # 'like_users' : [],            
                }

                serializer = MovieSaveSerializer(data=fields)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(user=request.user)

                # movie = Movie.objects.get(pk=movie['id'])
                # genres = movie['genre_ids']
                # for genre in genres:
                #     movie.genres.add(genre)
                
    sorted_products =  Movie.objects.all()
    serializer = MovieSaveSerializer(sorted_products, many=True)
    return Response(serializer.data)
                
    # return Response(response)