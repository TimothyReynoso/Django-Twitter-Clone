"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from authentication.views import LoginUser, LogoutUser

from twitteruser.views import HomePage, SignUpUser, UserProfile

from tweet.views import PostTweet, AllTweets, TweetDetails

from notification.views import Notifications

urlpatterns = [
    path('', HomePage.as_view(), name='Home'),
    path('admin/', admin.site.urls),
    path('login/', LoginUser, name='loginhere'),
    path('logout/', LogoutUser),
    path('signup/', SignUpUser, name='SignUp'),
    path('tweet/', PostTweet.as_view()),
    path('tweets/', AllTweets.as_view()),
    path('user-profile/<int:user_id>/', UserProfile.as_view(), name='User'),
    path('tweet-details/<int:tweet_id>/', TweetDetails, name='tweet'),
    path('notifications/', Notifications)
]