# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet

app_name = 'blog'

router = DefaultRouter()
router.register('posts', BlogPostViewSet, basename='blog-post')

urlpatterns = [
    path('', include(router.urls)),
]