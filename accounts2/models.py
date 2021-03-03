from django.db import models
from .validators import file_size
from django.utils import timezone

class Video(models.Model):

    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="videos/%y", validators=[file_size])

    def __str__(self):
        return self.caption

