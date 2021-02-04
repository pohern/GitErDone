from .models import List
from django.forms import ModelForm

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['body']