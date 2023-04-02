from django.urls import path
#from .views import HomePageView
from .views import (
    BlogListView,
    BlogDetailView,
    AboutPageView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path('blog/<int:pk>/delete/',BlogDeleteView.as_view(),name='blog_delete'),
    path('blog/<int:pk>/edit',BlogUpdateView.as_view(),name='blog_edit'),
    path('blog/new/',BlogCreateView.as_view(),name='blog_new'),
    path("blog/<int:pk>/",BlogDetailView.as_view(),name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(), name='about'),

    ]