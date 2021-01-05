from django.shortcuts import render

# Create your views here.
from tweet.forms import TweetForm
from tweet.models import Tweet

from twitteruser.models import MyUser

from notification.models import Notification

import re

def PostTweet(request):
    html = 'tweet.html'
    form = TweetForm
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(tweet_post=data['tweet'], tweeter=request.user)
            pattern = r'(@\w+)+'
            matches = re.findall(pattern, data['tweet'])
            """returns ['@tim', '@joe'] """
            for user in matches:
                if user[1:] in [_user.username for _user in MyUser.objects.all()]:
                    notify = Notification.objects.create(user_to_notify=MyUser.objects.get(username=user[1:]), tweet_to_notify=Tweet.objects.get(id=tweet.id))
            """ extract the username from the tweet with re
            if extracted user is in database we will create a notification for it
             """
    return render(request, html, {'form': form, 'request': request})


def AllTweets(request):
    html = 'all_tweets.html'
    tweets = Tweet.objects.all()
    return render(request, html, {'tweets': tweets, 'request': request})


def TweetDetails(request, tweet_id):
    html = 'tweet_details.html'
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, html, {'tweet':tweet, 'user':tweet.tweeter, 'request': request})