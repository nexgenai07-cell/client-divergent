# sitesettings/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import SiteSettings
from .serializers import SiteSettingsSerializer

class SiteSettingsView(generics.RetrieveAPIView):
    """Public endpoint to get site settings"""
    permission_classes = [AllowAny]
    serializer_class = SiteSettingsSerializer
    
    def get_object(self):
        settings = SiteSettings.objects.filter(is_active=True).first()
        if not settings:
            settings = SiteSettings.objects.create(
                site_name="Divergent Physics",
                copyright_text="© 2024 Divergent Physics. All rights reserved.",
                is_active=True
            )
        return settings

class SiteSettingsUpdateView(generics.UpdateAPIView):
    """Admin endpoint to update site settings"""
    permission_classes = [IsAdminUser]
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    
    def get_object(self):
        obj = SiteSettings.objects.first()
        if not obj:
            obj = SiteSettings.objects.create()
        return obj