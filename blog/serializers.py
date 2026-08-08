from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'description', 'content',
            'image', 'external_link', 'published_date', 'order',
        ]