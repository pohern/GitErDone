from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acounts/signup/', views.signup, name='signup'),
    path('lists/create/', views.ListCreate.as_view(), name='lists_create'),
    path('about/', views.about, name='about'),
    path('lists/<int:todolist_id>/', views.todolists_detail, name='detail'),
]