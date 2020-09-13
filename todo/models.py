from django.db import models
from django.urls import reverse


class Todo(models.Model):
    todo = models.CharField(max_length=200)

    def __str__(self):
        return self.todo

    def get_absolute_url(self):
        return reverse('home')
