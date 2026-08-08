# blog/admin.py
from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'read_time', 'published_date', 'is_active', 'order')
    list_filter = ('is_active', 'published_date')
    search_fields = ('title', 'author', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-published_date', 'order')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'read_time', 'description', 'content')
        }),
        ('Media & Links', {
            'fields': ('image', 'external_link')
        }),
        ('Publishing', {
            'fields': ('published_date', 'order', 'is_active')
        }),
    )