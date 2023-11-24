from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieSaveSerializer(serializers.ModelSerializer):
    class UserReplySerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname', 'age')
    user = UserReplySerializer(read_only=True)

    class Meta:
        model = Movie
        exclude = ('genre_check', )

class CommentSerializer(serializers.ModelSerializer):
    class UserCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname', 'age')



    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    # overide
    user = UserCommentSerializer(read_only=True)
    movie = MovieSerializer(read_only= True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        
class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'