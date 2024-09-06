import requests
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from .forms import CampusForm
from .models import campus

class CampusAdmin(admin.ModelAdmin):
    # form = CampusForm

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

    list_display = ('name', 'status', 'slug')  # Adjust according to your model fields

    def get_queryset(self, request):
        # Fetch campuses from FastAPI
        response = requests.get(f'{settings.FASTAPI_URL}/campus/')

        if response.status_code == 200:
            campuses = response.json()
            # Update or create Campus model instances
            for campus_data in campuses:
                # Assuming 'id' is a unique identifier and is part of the campus_data
                campus.objects.update_or_create(
                    # id=campus_data['_id'],  # Use 'id' or another unique field for matching
                    defaults={
                        'name': campus_data.get('name'),
                        'status': campus_data.get('status'),
                        'slug': campus_data.get('slug'),
                    }
                )
            # Return queryset of Campus objects
            return campus.objects.all()
        else:
            self.message_user(request, f"Error: {response.json()}", level='error')
            return campus.objects.none()  # Return empty queryset in case of an error

# Register your Campus model with the customized admin
admin.site.register(campus, CampusAdmin)
