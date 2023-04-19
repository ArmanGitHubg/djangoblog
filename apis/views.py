from rest_framework import generics
from pages.models import Blog
from .serializers import BlogSerializer

from django.shortcuts import render

# Create your views here.

class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer