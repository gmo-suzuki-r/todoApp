from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import todoModel

# Create your views here.


class todoList(ListView):
    template_name = 'list.html'
    model = todoModel


class todoDetail(DetailView):
    template_name = 'detail.html'
    model = todoModel
