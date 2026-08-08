from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('website.urls')),
    path('api/blog/', include('blog.urls')),
       path('api/projects/', include('projects.urls')),  # <-- Add this
        path('api/about/', include('about.urls')),
         path('api/platform/', include('platformm.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)