from django.urls import path

from .views import HomeView, CreateTodoView, DeleteTodoView, UpdateTodoView, delete_all_todos


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create-todo/', CreateTodoView.as_view(), name='create_todo'),
    path('delete-todo/<int:pk>/', DeleteTodoView.as_view(), name='delete_todo'),
    path('update-todo/<int:pk>/', UpdateTodoView.as_view(), name='update_todo'),
    path('delete-all/', delete_all_todos, name='delete_all'),
]
