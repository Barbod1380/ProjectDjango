from django.db import models
from django.urls import reverse
from datetime import date
import datetime


class Question(models.Model):
    now = datetime.datetime.now()
    title = models.CharField(max_length=100)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True, default=datetime.datetime.now())
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('TQD')




class Videos(models.Model):
    caption = models.CharField(max_length=100, null=True)
    vids = models.FileField(upload_to='videos')



class ANS(models.Model):
    FirstName = models.CharField(max_length=100, null=True)
    LastName = models.CharField(max_length=100, null=True)
    StudentNumber = models.CharField(max_length=100, null=True)
    WhichQuestion = models.ManyToManyField(Question)
    QuestionName = models.CharField(max_length=100)
    Grade = models.IntegerField()
    Sending_time = models.DateField(default=date.today)
    file = models.FileField(upload_to='books/pdfs/')



class CreateStudent(models.Model):
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    StudentNumber = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)

    def __str__(self):
        return (self.UserName)

class CreateTeacher(models.Model):
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)

    def __str__(self):
        return (self.UserName)













