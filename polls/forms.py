from django import forms
from django.forms import ModelForm
from .models import ANS, CreateStudent, CreateTeacher, Videos
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CreateVideo(ModelForm):
    class Meta:
        model = Videos
        fields='__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = ANS
        fields = ('FirstName', 'LastName', 'StudentNumber', 'QuestionName', 'Sending_time', 'file')


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = CreateStudent
        fields = ('UserName', 'Password', 'StudentNumber', 'Email')


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = CreateTeacher
        fields = ('UserName', 'Password', 'Email')


class Grade(ModelForm):
    class Meta:
        model = ANS
        fields = ['Grade']
