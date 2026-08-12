# sitesettings/models.py
from django.db import models
from website.models import BaseModel

class SiteSettings(BaseModel):
    """Singleton model for global site settings"""
    
    # Basic Info
    site_name = models.CharField(max_length=200, blank=True, null=True, default="Divergent Physics")
    site_description = models.TextField(blank=True, null=True)
    
    # Logo & Branding (Image uploads)
    logo = models.ImageField(upload_to='settings/', blank=True, null=True, help_text="Main site logo (upload image)")
    logo_dark = models.ImageField(upload_to='settings/', blank=True, null=True, help_text="Dark version of logo for light backgrounds")
    favicon = models.ImageField(upload_to='settings/', blank=True, null=True, help_text="Browser favicon (upload image)")
    
    # Contact Information
    email = models.EmailField(blank=True, null=True, help_text="General contact email")
    phone = models.CharField(max_length=50, blank=True, null=True, help_text="Contact phone number")
    location = models.CharField(max_length=500, blank=True, null=True, help_text="Physical address or location")
    
    # Footer
    footer_description = models.TextField(blank=True, null=True, help_text="Footer description text")
    copyright_text = models.CharField(max_length=200, blank=True, null=True, default="© 2024 Divergent Physics. All rights reserved.")
    
    # Social Links (Individual fields)
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter/X URL")
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
    github = models.URLField(blank=True, null=True, help_text="GitHub URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube URL")
    tiktok = models.URLField(blank=True, null=True, help_text="TikTok URL")
    
    # CTAs
    calendar_link = models.URLField(blank=True, null=True, help_text="Booking/calendar link (e.g., Calendly)")
    contact_form_cta = models.CharField(max_length=100, blank=True, null=True, default="Book a Consultation →")
    
    # SEO
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    
    # Active status
    is_active = models.BooleanField(default=True)
    
    def get_social_links(self):
        """Return social links as a dictionary"""
        return {
            'linkedin': self.linkedin,
            'twitter': self.twitter,
            'facebook': self.facebook,
            'instagram': self.instagram,
            'github': self.github,
            'youtube': self.youtube,
            'tiktok': self.tiktok,
        }
    
    def __str__(self):
        return self.site_name if self.site_name else "Site Settings"
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"