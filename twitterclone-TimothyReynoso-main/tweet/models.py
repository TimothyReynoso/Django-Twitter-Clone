from django.db import models
from django.utils import timezone

# Create your models here.
from twitteruser.models import MyUser


class Tweet(models.Model):
    tweet_post = models.CharField(max_length=140)
    date = models.DateTimeField(default=timezone.now)
    tweeter = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tweet_post} - By: {self.tweeter}'