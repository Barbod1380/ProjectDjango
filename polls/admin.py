from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Videos, ANS, Question
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

admin.site.register(Videos)
admin.site.register(ANS)
admin.site.register(Question)

