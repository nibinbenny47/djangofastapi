# from django import forms
 
# class CampusForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     status = forms.ChoiceField(
#         choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
#         label='Status'
#     )
#     slug = forms.SlugField(max_length=100)

from django import forms
from .models import campus

class CampusForm(forms.ModelForm):
    class Meta:
        model = campus
        fields = ['name', 'status', 'slug']
