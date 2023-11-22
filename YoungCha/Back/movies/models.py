from django.db import models
from django.conf import settings

class Movies(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()

class MovieComment(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)

    user_rating = models.DecimalField(max_digits=3, decimal_places=2)  # DecimalField로 변경

    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_comments')  # ManyToManyField로 변경

    def like_comment(self, user):
        self.liked_users.add(user)

    def unlike_comment(self, user):
        self.liked_users.remove(user)

    def is_liked_by_user(self, user):
        return self.liked_users.filter(pk=user.pk).exists()