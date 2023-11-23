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
from .serializers import RateSerializer, CommentSerializer

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




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_rating_and_comment(request, movie_id):
    try:
        rating = request.data.get('rating')
        comment = request.data.get('comment')

        # 영화에 대한 평점 저장
        movie = Movie.objects.get(pk=movie_id)
        rate = Rate.objects.create(rate_user=request.user, rate_movie=movie, rate_score=rating)

        # 영화에 대한 코멘트 저장
        comment = Comment.objects.create(user=request.user, movie=movie, content=comment)
        comment_serializer = CommentSerializer(comment, many=False)
        rate_serializer = RateSerializer(rating, many=True)
        movie_serializer=MovieSerializer(movie)
        return Response({'message': 'Rating and comment saved successfully.'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_movie_ratings_and_comments(request, movie_id):
    try:
        # 특정 영화에 대한 평점 조회
        rates = Rate.objects.filter(rate_movie_id=movie_id)
        rate_serializer = RateSerializer(rates, many=True)

        # 특정 영화에 대한 코멘트 조회
        comments = Comment.objects.filter(movie_id=movie_id)
        comment_serializer = CommentSerializer(comments, many=True)

        return Response({
            'rates': rate_serializer.data,
            'comments': comment_serializer.data
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)