from django.urls import path
from . import views


urlpatterns = [
    path('community/', views.community_list),
    path('community/<int:community_pk>/', views.community_detail),
    path('community/<int:community_pk>/like/', views.community_like),
    path('community/<int:community_pk/like_count/', views.community_like_count),

    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('comments/<int:comment_pk>/like/', views.comment_like),
    path('comments/<int:comment_pk>/like_count/', views.comment_like_count),
    path('community/<int:community_pk>/create/', views.comment_create),


    path('reply/', views.reply_list),
    path('reply/<int:reply_pk>/', views.reply_detail),
    path('reply/<reply_pk>/like/', views.reply_like),
    path('reply/<reply_pk>/like_count/', views.reply_like_count),
    path('comments/<comment_pk>/create/', views.reply_create),
]
