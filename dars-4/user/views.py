from django.shortcuts import render
from .models import Home
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

class HomeView(ListView):
    model = Home
    template_name = 'home.html'

class HomeDetailView(DetailView):
    model = Home
    template_name = 'home_detail.html'

class BlogCreateView(CreateView):
    model = Home
    template_name = 'create_post.html'
    fields = ['title', 'author', 'text']

class BlogUpdate(UpdateView):
    model = Home
    template_name = 'edit_post.html'
    fields = ['title', 'text']


