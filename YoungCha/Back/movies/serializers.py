from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

# class MovieListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movies
#         fields = ('title', 'overview')

# class MovieCommentListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MovieComment
#         fields = ('nickname', 'comments', 'created_at')  # 'comment' 필드가 'comments'로 변경되었습니다.

# class MovieCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MovieComment
#         fields = ('nickname', 'user_rating', 'comments', 'created_at', 'liked_users')  # 필드 목록에 'user_rating'과 'liked_users'를 추가하였습니다.


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
        exclude = ('genres', )
        