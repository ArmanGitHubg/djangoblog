from django.urls import path
#from .views import HomePageView
from .views import BlogListView, BlogDetailView,AboutPageView

urlpatterns = [
    path("blog/<int:pk>/",BlogDetailView.as_view(),name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(), name='about'),

    ]