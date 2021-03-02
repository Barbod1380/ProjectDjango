from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['username', 'password', 'email', 'Student_Number']
