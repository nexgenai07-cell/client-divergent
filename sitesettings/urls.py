# sitesettings/urls.py
from django.urls import path
from .views import SiteSettingsView, SiteSettingsUpdateView

app_name = 'sitesettings'

urlpatterns = [
    # Public endpoint - Get site settings
    path('', SiteSettingsView.as_view(), name='site_settings'),
    
    # Admin endpoint - Update site settings (requires authentication)
    path('update/', SiteSettingsUpdateView.as_view(), name='site_settings_update'),
]