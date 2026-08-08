# blog/serializers.py
from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'id', 
            'title', 
            'slug', 
            'description', 
            'content',
            'image', 
            'external_link', 
            'author',          # New field
            'read_time',       # New field
            'published_date', 
            'order',
            'is_active',
        ]