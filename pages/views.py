# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView, DetailView,TemplateView
)
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Blog

# Create your views here.

# def homePageView(request):
#     return HttpResponse("<h1>hello world<h1>")

class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name ='blog_new.html'
    fields = ['title','author', 'body']

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')