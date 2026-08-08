# projects/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'projects'

router = DefaultRouter()
router.register(r'sections', views.ProjectSectionViewSet)
router.register(r'cards', views.ProjectCardViewSet)

urlpatterns = [
    # All CRUD endpoints
    path('', include(router.urls)),
    
    # Public endpoints
    path('sections/', views.ProjectSectionListView.as_view(), name='project_sections_list'),
    path('cards/', views.ProjectCardListView.as_view(), name='project_cards_list'),
]