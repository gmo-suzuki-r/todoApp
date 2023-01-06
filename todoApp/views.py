from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import todoModel
from django.urls import reverse_lazy

# Create your views here.


class todoList(ListView):
    template_name = 'list.html'
    model = todoModel


class todoDetail(DetailView):
    template_name = 'detail.html'
    model = todoModel


class todoCreate(CreateView):
    template_name = 'create.html'
    model = todoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')


class todoDelete(DeleteView):
    template_name = 'delete.html'
    model = todoModel
    success_url = reverse_lazy('list')


class todoUpdate(UpdateView):
    template_name = 'update.html'
    model = todoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
