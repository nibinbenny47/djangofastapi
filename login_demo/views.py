import requests
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from django.conf import settings


def login_create(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            response = requests.post(
                f'{settings.FASTAPI_URL}/auth/token',
                data={
                    'username':username,
                    'password':password
                }
            )
            if response.status_code == 200:
                tokens = response.json()
                request.session['access_token'] = tokens['access_token']
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                return render(request,'login.html',{'form':form,'error':'Invalid credentials' })
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

# Create your views here.
