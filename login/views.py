# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterUser, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

User = get_user_model()

def register_teacher(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.email}")
    if request.method == 'POST':
        form = RegisterUser(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # adding the new teacher to teacher Group---------------------------------------
            new_group = Group.objects.get(name = 'Teacher')
            user = User.objects.get(id=user.id)
            new_group.user_set.add(user)

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/department/')
            else:
                messages.error(request, 'Authentication failed. Please try again.')
                print("hi")
            # login(request, user)
            # return redirect('/department/')
    else:
        form = RegisterUser()
    return render(request, 'auth/register.html', {'form': form})


def register_admin(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.email}")
    if request.method == 'POST':
        form = RegisterUser(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # adding the new student to Student Group---------------------------------------
            new_group = Group.objects.get(name = 'Admin')
            user = User.objects.get(id=user.id)
            new_group.user_set.add(user)
            
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/department/')
            else:
                messages.error(request, 'Authentication failed. Please try again.')
                print("hi")
            # login(request, user)
            # return redirect('/department/')
    else:
        form = RegisterUser()
    return render(request, 'auth/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                
                # Print the username and address of the logged-in user
                print(f"Username: {user.username}")
                print(f"Address: {user.address}")
                
                group_name = Group.objects.all().filter(
                    user=request.user
                )# get logged user grouped name
                group_name = str(group_name[0])  # convert to string
                print(group_name)

                # if next_url is given after login it will redirect to the specific -------------------------------------------------
                # module we given in url other than redirect to dashboard----------------------------------------------

                next_url = request.GET.get('next')
                if next_url: 
                    return redirect(next_url)
                # Redirect based on user roles---------------------------------------
                if user.is_superuser:
                    return redirect('/exam/')
                elif group_name == 'Teacher':
                    return redirect('/teacher/')
                else:
                    return render(request,'admin/dashboard.html')
                
            # Handle invalid credentials
            form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'auth/login.html', {'form': form})


# trying to disable back button after logout ----------------------------------------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_logout(request):
    logout(request)
    return redirect('index')