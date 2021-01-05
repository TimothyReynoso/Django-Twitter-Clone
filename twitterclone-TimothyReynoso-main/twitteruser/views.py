from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
from twitteruser.forms import SignUpForm
from twitteruser.models import MyUser
from tweet.models import Tweet

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# @login_required(login_url='/login/')
# def HomePage(request):
#     html = 'index.html'
#     loggedin_user = MyUser.objects.get(id=request.user.id)
#     following = loggedin_user.followers.all()
#     follower_tweets = []
#     for user in following:
#         follower_tweets += Tweet.objects.filter(tweeter=user)
#     return render(request, html, {'request': request, 'follower_tweets': follower_tweets})

# @method_decorator(login_required(login_url='/login/')) 
class HomePage(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        html = 'index.html'
        loggedin_user = MyUser.objects.get(id=request.user.id)
        following = loggedin_user.followers.all()
        # def myFunc(e, a):
        #     return e[a].date.toordinal()
        follower_tweets = []
        for user in following:
            follower_tweets += Tweet.objects.filter(tweeter=user)
       
        # new_list = []
        # for num in range(len(follower_tweets)):
        #     new_list += follower_tweets.sort(key=myFunc(e=follower_tweets, a=num))
        return render(request, html, {'request': request, 'follower_tweets': follower_tweets[::-1]})


def SignUpUser(request):
    html = 'signup.html'
    form = SignUpForm
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data['username'], first_name=data['displayname'], email=data['email'], password=data['password'])
            user = authenticate(
                username=data['username'], password=data['password'])
            logout(request)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('Home'))
    return render(request, html, {'form': form, 'request': request})


# def UserProfile(request, user_id):
#     html = 'user_details.html'
#     loggedin_user = MyUser.objects.get(id=request.user.id)
#     user = MyUser.objects.get(id=user_id)
#     user_tweets = Tweet.objects.filter(tweeter=user)
#     if request.method == 'POST':
#         if len(loggedin_user.followers.filter(username=user)) == 0:
#             loggedin_user.followers.add(user)
#             loggedin_user.save()
#         else:
#             loggedin_user.followers.remove(user)
#             loggedin_user.save()
#         """ if 'is following than unfollow' and else follow or vis versa"""
#     return render(request, html, {'user_tweets': user_tweets, 'user': user, 'request': request})

class UserProfile(View):
    def get(self, request, user_id):
        html = 'user_details.html'
        loggedin_user = MyUser.objects.get(id=request.user.id)
        user = MyUser.objects.get(id=user_id)
        user_tweets = Tweet.objects.filter(tweeter=user)
        if loggedin_user in user.followers.all():
            following = True
        else:
            following = False
        return render(request, html, {'user_tweets': user_tweets, 'user': user, 'request': request, 'total_tweets': len(user_tweets), 'total_followers': len(user.followers.all()), 'following': following}) 



    def post(self, request, user_id):
        html = 'user_details.html'
        loggedin_user = MyUser.objects.get(id=request.user.id)
        user = MyUser.objects.get(id=user_id)
        user_tweets = Tweet.objects.filter(tweeter=user)
        if len(loggedin_user.followers.filter(username=user)) == 0:
            loggedin_user.followers.add(user)
            loggedin_user.save()
            following = True
            return render(request, html, {'user_tweets': user_tweets, 'user': user, 'request': request, 'total_tweets': len(user_tweets), 'total_followers': len(user.followers.all()), 'following': following})
        else:
            loggedin_user.followers.remove(user)
            loggedin_user.save()
            following = False
        """ if 'is following than unfollow' and else follow or vis versa"""
        return render(request, html, {'user_tweets': user_tweets, 'user': user, 'request': request, 'total_tweets': len(user_tweets), 'total_followers': len(user.followers.all()), 'following': following}) 

def FollowUser(request):
    pass