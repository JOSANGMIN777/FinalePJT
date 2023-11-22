from rest_framework.response import Response
from rest_framework import status

# permission Decorators
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count
from django.http import JsonResponse

from .serializers import *
from .models import *


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def community_list(request):
    if request.method == 'GET':
        communitys = get_list_or_404(Community)
        serializer = CommunityListSerializer(communitys, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def community_detail(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)

    if request.method == 'GET':
        serializer = CommunitySerializer(community)
        print(serializer.data)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def community_like(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    if community.like_community_users.filter(pk=request.user.pk).exists():
        community.like_community_users.remove(request.user)
    else:
        community.like_community_users.add(request.user)
    
    serializer = CommunitySerializer(community)

    like_status = {
        'id': serializer.data.get('id'),
        'count': community.like_community_users.count(),
        'like_list': serializer.data.get('like_review_users'),
    }
    return JsonResponse(like_status)



@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_list(request):
    # comments = Comment.objects.all()
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(community=community, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_like(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if comment.like_comment_users.filter(pk=request.user.pk).exists():
        comment.like_comment_users.remove(request.user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else:
        comment.like_comment_users.add(request.user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_like_count(request, comment_pk):
    comments = Comment.objects.annotate(
        like_comment_users_count = Count('like_comment_users', distinct=True)
    )

    comment = comments.get(pk=comment_pk)
    serializer = CommentLikeSerialzer(comment)
    return Response(serializer.data)


@api_view(['GET'])
def reply_list(request):
    # comments = Comment.objects.all()
    replies = get_list_or_404(Reply)
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def reply_detail(request, reply_pk):
    reply = get_object_or_404(Reply, pk=reply_pk)
    if request.method == 'GET':
        serializer = ReplySerializer(reply)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reply_create(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(comment=comment, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reply_like(request, reply_pk):
    reply = get_object_or_404(Reply, pk=reply_pk)

    if reply.like_reply_users.filter(pk=request.user.pk).exists():
        reply.like_reply_users.remove(request.user)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)
    else:
        reply.like_reply_users.add(request.user)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def reply_like_count(request, reply_pk):
    replies = Reply.objects.annotate(
        like_reply_users_count = Count('like_reply_users', distinct=True)
    )

    reply = replies.get(pk=reply_pk)
    serializer = ReplyLikeSerialzer(reply)
    return Response(serializer.data)