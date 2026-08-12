# sitesettings/admin.py
from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'email', 'phone', 'is_active', 'created_at', 'updated_at')
    list_editable = ('is_active',)
    search_fields = ('site_name', 'email', 'phone', 'location')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'site_description', 'is_active')
        }),
        ('Branding (Upload Images)', {
            'fields': ('logo', 'logo_dark', 'favicon'),
            'description': 'Upload your logo images here. Logo will be displayed in header, dark logo for light backgrounds.'
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Footer', {
            'fields': ('footer_description', 'copyright_text')
        }),
        ('Social Links', {
            'fields': ('linkedin', 'twitter', 'facebook', 'instagram', 'github', 'youtube', 'tiktok'),
            'description': 'Enter full URLs for your social media profiles'
        }),
        ('CTAs & Booking', {
            'fields': ('calendar_link', 'contact_form_cta')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        return False