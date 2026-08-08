from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published_date', 'is_active', 'order')
    prepopulated_fields = {'slug': ('title',)}