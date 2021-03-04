from django.db import models
from .validators import file_size
from django.urls import reverse


class Video(models.Model):

    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="videos/%y", validators=[file_size])

    def __str__(self):
        return self.caption


class Questions(models.Model):

    title = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


