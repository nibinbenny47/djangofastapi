from django import forms
 
class CampusForm(forms.Form):
    name = forms.CharField(max_length=100)
    status = forms.ChoiceField(
        choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
        label='Status'
    )
    slug = forms.SlugField(max_length=100)
