# blog/views.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.filter(is_active=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]