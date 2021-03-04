from django.db import models
from .validators import file_size
from ckeditor.fields import RichTextField

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
