from django.contrib import admin
from .models import TodoList, Rating
# Register your models here.

admin.site.register(TodoList)
admin.site.register(Rating)