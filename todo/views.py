# from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from .models import Todo
from .forms import TodoForm


class HomeView(ListView):
    model = Todo
    template_name = 'home.html'


class CreateTodoView(CreateView):
    model = Todo
    fields = ('todo',)
    success_url = reverse_lazy('home')


class DeleteTodoView(DeleteView):
    model = Todo
    success_url = reverse_lazy('home')

    # to convert todo for delete without confirmation template when using class based deleteview
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UpdateTodoView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'update-todo.html'
    # fields = ['todo']


def delete_all_todos(request):
    todos = Todo.objects.all()
    todos.delete()

    return redirect('home')
