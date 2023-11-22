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
    

# class Genre(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)


# class Movie(models.Model):
    
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=100)
#     release_date = models.DateField(null=True, blank=True)
#     popularity = models.FloatField(null=True, blank=True)
#     overview = models.TextField(null=True, blank=True)
#     vote_average = models.FloatField(null=True, blank=True)
#     vote_count = models.IntegerField(null=True, blank=True)
#     poster_path = models.CharField(max_length=200, null=True, blank=True)

#     video_url = models.CharField(max_length=200, null=True, blank=True)


#     register_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='register_movies', default=1)

#     genre_check = models.ManyToManyField(Genre, related_name='genre_movies')

#     like_movie_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
#     rates_users = models.ManyToManyField('accounts.User', related_name='user_rated_movie', through='Rate')

    


# class Rate(models.Model):
#     rate_user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_rated')
#     rate_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     rate_score = models.FloatField()