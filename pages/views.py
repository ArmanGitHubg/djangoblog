# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView,TemplateView
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