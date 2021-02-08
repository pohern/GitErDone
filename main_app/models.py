from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'todolist_id': self.id})

    def __str__(self):
        return self.name

class Rating(models.Model):
    items = models.CharField(max_length=250)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.items

    def get_absolute_url(self):
        return reverse('detail', kwargs={'todolist_id' : self.id})