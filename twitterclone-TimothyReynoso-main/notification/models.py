from django.db import models

from twitteruser.models import MyUser
from tweet.models import Tweet

# Create your models here.
class Notification(models.Model):
    user_to_notify = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_to_notify')
    tweet_to_notify = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweet_to_notify')
    notified_flag = models.BooleanField(default=False)


    def __str__(self):
        return f'Notify: {self.user_to_notify} Tweet: {self.tweet_to_notify}'