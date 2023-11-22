from rest_framework import serializers
from .models import Community, Comment, Reply
from django.contrib.auth import get_user_model

class CommunityListSerializer(serializers.ModelSerializer):
    class UserCommunitySerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname', 'age')
    user = UserCommunitySerializer(read_only=True)

    class Meta:
        model = Community
        fields = ('id', 'user', 'title', 'content', 'comments',)


class ReplySerializer(serializers.ModelSerializer):
    class UserReplySerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname', 'age')
    user = UserReplySerializer(read_only=True)
    
    class CommentReplySerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'

    comment = CommentReplySerializer(read_only=True)

    class Meta:
        model = Reply
        fields = '__all__'
        read_only_fields = ('comment', 'user',)


class CommentSerializer(serializers.ModelSerializer):
    class UserCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname', 'age')
    user = UserCommentSerializer(read_only=True)
    replies = ReplySerializer(many=True, read_only=True)
    replies_count = serializers.IntegerField(source='replies.count', read_only=True)
    
    class CommunityCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Community
            fields = ('id', 'title', 'content', 'user')

    community = CommunityCommentSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('community', 'user',)


class CommunitySerializer(serializers.ModelSerializer):
    class UserCommunitySerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname', 'age')

    
    like_community_users = UserCommunitySerializer(many=True, read_only=True)

    user = UserCommunitySerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    
    class Meta:
        model = Community
        fields = '__all__'
        read_only_fields = ('user',)


class CommunityLikeSerializer(serializers.ModelSerializer):
    class UserCommunitySerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname', 'age')
        
    like_community_users = UserCommunitySerializer(many=True, read_only=True)

    class Meta:
        model = Community
        fields = ('id', 'likes_community_users')


class CommentLikeSerialzer(serializers.ModelSerializer):

    like_comment_users_count = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ('id', 'like_comment_users_count', 'content')


class ReplyLikeSerialzer(serializers.ModelSerializer):

    like_reply_users_count = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ('id', 'like_reply_users_count', 'content')