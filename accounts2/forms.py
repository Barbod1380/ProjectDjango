from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Video, Questions

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']



class Question_form(forms.Form):
    class Meta:
        model = Questions
        fields = ("title", "body")

class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("caption","video")
