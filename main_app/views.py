from django.shortcuts import render, redirect
from .models import TodoList
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ListCreate(LoginRequiredMixin, CreateView):
  model = TodoList
  fields = ['name', 'description']

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
    # success_url = '/cats/' on method, best is in model though

def about(request):
    return render(request, 'about.html')

@login_required
def todolists_index(request):
    todolists = TodoList.objects.filter(user=request.user)
    return render(request, 'todolist/index.html', { 'todolists': todolists })

@login_required
def todolists_detail(request, todolist_id):
    todolist = TodoList.objects.get(id=todolist_id)
    return render(request, 'todolist/detail.html', {'todolist': todolist})

