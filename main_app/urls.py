from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acounts/signup/', views.signup, name='signup'),
    path('lists/create/', views.ListCreate.as_view(), name='lists_create'),
    path('about/', views.about, name='about'),
    path('lists/', views.todolists_index, name='index'),
    path('lists/<int:todolist_id>/', views.todolists_detail, name='detail'),
    path('lists/<int:pk>/update/', views.TodoListUpdate.as_view(), name='todolists_update'),
    path('lists/<int:pk>/delete/', views.TodoListDelete.as_view(), name='todolists_delete'),
    path('lists/<int:todolist_id>/add_item', views.add_item, name='add_item'),
]