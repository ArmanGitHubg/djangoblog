from rest_framework import serializers

from pages.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = ('title', 'author', 'body')