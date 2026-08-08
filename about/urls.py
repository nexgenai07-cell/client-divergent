# about/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'about'

router = DefaultRouter()
router.register(r'sections', views.AboutSectionViewSet)
router.register(r'team-members', views.TeamMemberViewSet)
router.register(r'publications', views.PublicationViewSet)
router.register(r'patents', views.PatentViewSet)
router.register(r'stats', views.AboutStatViewSet)

urlpatterns = [
    # All CRUD endpoints
    path('', include(router.urls)),
    
    # Public endpoints
    path('sections/', views.AboutSectionListView.as_view(), name='about_sections_list'),
    path('team-members/', views.TeamMemberListView.as_view(), name='team_members_list'),
    path('publications/', views.PublicationListView.as_view(), name='publications_list'),
    path('patents/', views.PatentListView.as_view(), name='patents_list'),
    path('stats/', views.AboutStatListView.as_view(), name='about_stats_list'),
]