# sitesettings/serializers.py
from rest_framework import serializers
from .models import SiteSettings

class SiteSettingsSerializer(serializers.ModelSerializer):
    social_links = serializers.SerializerMethodField()
    
    class Meta:
        model = SiteSettings
        fields = [
            'id',
            'site_name',
            'site_description',
            'logo',
            'logo_dark',
            'favicon',
            'email',
            'phone',
            'location',
            'footer_description',
            'copyright_text',
            'linkedin',
            'twitter',
            'facebook',
            'instagram',
            'github',
            'youtube',
            'tiktok',
            'social_links',  # Computed field
            'calendar_link',
            'contact_form_cta',
            'meta_title',
            'meta_description',
            'meta_keywords',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def get_social_links(self, obj):
        """Return all social links as a dictionary"""
        return {
            'linkedin': obj.linkedin,
            'twitter': obj.twitter,
            'facebook': obj.facebook,
            'instagram': obj.instagram,
            'github': obj.github,
            'youtube': obj.youtube,
            'tiktok': obj.tiktok,
        }