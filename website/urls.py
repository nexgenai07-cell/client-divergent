from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PageViewSet, SectionViewSet, SectionItemViewSet,
    NavLinkViewSet, PricingPlanViewSet, LeadViewSet, SiteSettingsView
)

router = DefaultRouter()
router.register('pages', PageViewSet, basename='page')
router.register('sections', SectionViewSet, basename='section')
router.register('section-items', SectionItemViewSet, basename='section-item')
router.register('nav-links', NavLinkViewSet, basename='nav-link')
router.register('pricing-plans', PricingPlanViewSet, basename='pricing-plan')
router.register('leads', LeadViewSet, basename='lead')

urlpatterns = [
    path('site-settings/', SiteSettingsView.as_view(), name='site-settings'),
    path('', include(router.urls)),
]