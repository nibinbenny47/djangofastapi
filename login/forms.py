from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegisterUser(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(max_length=255, required=True)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'phone', 'date_of_birth', 'address', 'profile_image', 'password1', 'password2')

