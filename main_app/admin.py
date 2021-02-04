from django.contrib import admin
from .models import TodoList, List
# Register your models here.

admin.site.register(TodoList)
admin.site.register(List)