import requests
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from .forms import CampusForm
from .models import campus

class CampusAdmin(admin.ModelAdmin):
    form = CampusForm

    def save_model(self, request, obj, form, change):
        access_token = request.session.get('access_token')
        if not access_token:
            self.message_user(request, "Access token not found. Please log in.")
            return HttpResponseRedirect('/admin/login/')  # Redirect if no token

        # Collect form data to send to FastAPI
        data = {
            'name': form.cleaned_data['name'],
            'status': form.cleaned_data['status'],
            'slug': form.cleaned_data['slug'],
        }

        # Make a POST request to the FastAPI backend
        response = requests.post(
            f'{settings.FASTAPI_URL}/campus/',
            headers={'Authorization': f'Bearer {access_token}'},
            data=data
        )

        if response.status_code == 200:
            self.message_user(request, "Campus added successfully to MongoDB!")
        else:
            self.message_user(request, f"Error: {response.json()}", level='error')

    def get_queryset(self, request):
        return campus.objects.none()  # Disable querying from Django's database

# Register your Campus model with the customized admin
admin.site.register(campus, CampusAdmin)
