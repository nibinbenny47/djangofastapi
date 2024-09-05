import requests
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from .forms import CampusForm

def campus_create(request):
    if request.method == 'POST':
        print("hi")
        form = CampusForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = form.cleaned_data['name']
            status = form.cleaned_data['status']
            slug = form.cleaned_data['slug']
            access_token = request.session.get('access_token')
            print(access_token)
            if not access_token:
                return redirect('campus_create')
            response = requests.post(
                f'{settings.FASTAPI_URL}/campus/',
                headers= {'Authorization':f'Bearer {access_token}'},
                data ={
                    'name':data['name'],
                    'status':data['status'],
                    'slug':data['slug']
                }
            )
            if response.status_code == 200:

                return HttpResponseRedirect(reverse('admin:index'))
            else:
                return render(request,'error.html',{'error':response.json()})
    else:
        form = CampusForm()
    return render(request,'submit_campus.html',{'form':form})

# Create your views here.
