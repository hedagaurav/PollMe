from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserRegistrationForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        # print(request.POST)
        # we can change the default value for username and password by passing values instead of None.
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            # return HttpResponseRedirect(reverse('home'))
            return redirect(redirect_url)
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, 'accounts/login.html', {})


def user_logout(request):
    logout(request)
    return redirect('accounts:login')
    # return render(request, 'accounts/logout.html', {})


def user_registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']

            # user = User.objects.create_user(username,None, password)
            # use above syntax or use below syntax
            user = User.objects.create_user(username, email=email, password=password)
            messages.success(request, 'Thank you for registering {}'.format(user.username))
            # when the user is successfully registered the user is redirected to login page
            return redirect('accounts:login')

    else:
        form = UserRegistrationForm()
    #   messages.error(request, 'Something went wrong.')
    return render(request, 'accounts/register.html', {'form': form})
