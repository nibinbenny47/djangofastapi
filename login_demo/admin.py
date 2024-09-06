from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
import requests
from django.conf import settings

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # Use the custom form when adding a user
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'full_name', 'password1', 'password2'),
        }),
    )

    def save_model(self, request, obj, form, change):
        # Save the user in Django's database
        super().save_model(request, obj, form, change)

        # Prepare the data to send to FastAPI
        user_data = {
            'username': form.cleaned_data['username'],
            'email': form.cleaned_data['email'],
            'full_name': form.cleaned_data['full_name'],
            'password': form.cleaned_data['password1'],
            'phone':form.cleaned_data['phone'], # Sending plain password (you may hash it before sending to FastAPI),
        }

        # Send the data to FastAPI to store in MongoDB
        try:
            response = requests.post(
                f'{settings.FASTAPI_URL}/auth/register',
                data=user_data)
            if response.status_code != 200:
                raise Exception(f"Failed to register user in FastAPI: {response.content}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error communicating with FastAPI: {e}")
        
# Unregister the old User admin and register the new one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

