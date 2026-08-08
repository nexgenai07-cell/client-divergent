# platform/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'platform'

router = DefaultRouter()
router.register(r'sections', views.PlatformSectionViewSet)
router.register(r'operating-benefits', views.OperatingBenefitViewSet)
router.register(r'work-with-us', views.WorkWithUsViewSet)
router.register(r'coming-soon', views.ComingSoonViewSet)
router.register(r'demonstrations', views.DemonstrationViewSet)
router.register(r'built-for-production', views.BuiltForProductionViewSet)
router.register(r'pricing-plans', views.PricingPlanViewSet)

urlpatterns = [
    # All CRUD endpoints
    path('', include(router.urls)),
    
    # Public endpoints
    path('sections/', views.PlatformSectionListView.as_view(), name='platform_sections_list'),
    path('operating-benefits/', views.OperatingBenefitListView.as_view(), name='operating_benefits_list'),
    path('work-with-us/', views.WorkWithUsListView.as_view(), name='work_with_us_list'),
    path('coming-soon/', views.ComingSoonListView.as_view(), name='coming_soon_list'),
    path('demonstrations/', views.DemonstrationListView.as_view(), name='demonstrations_list'),
    path('built-for-production/', views.BuiltForProductionListView.as_view(), name='built_for_production_list'),
    path('pricing-plans/', views.PricingPlanListView.as_view(), name='pricing_plans_list'),
]