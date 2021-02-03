from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'todolist_id': self.id})

    def __str__(self):
        return self.name