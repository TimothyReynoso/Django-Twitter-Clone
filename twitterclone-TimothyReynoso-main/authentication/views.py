from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
from authentication.forms import LoginForm

from django.contrib.auth import authenticate, login, logout


def LoginUser(request):
    html = 'login_page.html'
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('Home'))
    return render(request, html, {'form': form, 'request': request})


def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))