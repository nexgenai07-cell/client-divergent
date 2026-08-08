# website/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'website'

# Create router for ViewSets
router = DefaultRouter()
router.register(r'hero', views.HeroSectionViewSet)
router.register(r'pipeline-steps', views.PipelineStepViewSet)
router.register(r'problem-statements', views.ProblemStatementViewSet)
router.register(r'problem-quotes', views.ProblemQuoteViewSet)
router.register(r'statistics', views.StatisticViewSet)
router.register(r'stat-items', views.StatItemViewSet)
router.register(r'field-notes', views.FieldNoteViewSet)
router.register(r'field-note-items', views.FieldNoteItemViewSet)
router.register(r'service-sections', views.ServiceSectionViewSet)
router.register(r'service-cards', views.ServiceCardViewSet)
router.register(r'case-studies', views.CaseStudyViewSet)
router.register(r'case-study-cards', views.CaseStudyCardViewSet)
router.register(r'asset-sections', views.AssetSectionViewSet)
router.register(r'asset-items', views.AssetItemViewSet)
router.register(r'how-we-work', views.HowWeWorkViewSet)
router.register(r'how-we-work-steps', views.HowWeWorkStepViewSet)
router.register(r'why-us-sections', views.WhyUsSectionViewSet)
router.register(r'why-us-cards', views.WhyUsCardViewSet)
router.register(r'platforms', views.OurPlatformViewSet)
router.register(r'platform-features', views.PlatformFeatureViewSet)
router.register(r'faqs', views.FAQViewSet)
router.register(r'get-started', views.GetStartedSectionViewSet)

urlpatterns = [
    # All CRUD endpoints
    path('', include(router.urls)),
    
    # Combined Website Data - All data in one endpoint
    path('website-data/', views.WebsiteDataView.as_view(), name='website_data'),
    
    # Individual public endpoints
    path('hero/', views.HeroListView.as_view(), name='hero_list'),
    path('pipeline-steps/', views.PipelineStepListView.as_view(), name='pipeline_steps_list'),
    path('problem-statements/', views.ProblemStatementListView.as_view(), name='problem_statement_list'),
    path('problem-quotes/', views.ProblemQuoteListView.as_view(), name='problem_quotes_list'),
    path('statistics/', views.StatisticsListView.as_view(), name='statistics_list'),
    path('stat-items/', views.StatItemListView.as_view(), name='stat_items_list'),
    path('field-notes/', views.FieldNoteListView.as_view(), name='field_notes_list'),
    path('field-note-items/', views.FieldNoteItemListView.as_view(), name='field_note_items_list'),
    path('service-sections/', views.ServiceSectionListView.as_view(), name='service_sections_list'),
    path('service-cards/', views.ServiceCardListView.as_view(), name='service_cards_list'),
    path('case-studies/', views.CaseStudyListView.as_view(), name='case_studies_list'),
    path('case-study-cards/', views.CaseStudyCardListView.as_view(), name='case_study_cards_list'),
    path('asset-sections/', views.AssetSectionListView.as_view(), name='asset_sections_list'),
    path('asset-items/', views.AssetItemListView.as_view(), name='asset_items_list'),
    path('how-we-work/', views.HowWeWorkListView.as_view(), name='how_we_work_list'),
    path('how-we-work-steps/', views.HowWeWorkStepListView.as_view(), name='how_we_work_steps_list'),
    path('why-us-sections/', views.WhyUsSectionListView.as_view(), name='why_us_sections_list'),
    path('why-us-cards/', views.WhyUsCardListView.as_view(), name='why_us_cards_list'),
    path('platforms/', views.PlatformListView.as_view(), name='platforms_list'),
    path('platform-features/', views.PlatformFeatureListView.as_view(), name='platform_features_list'),
    path('faqs/', views.FAQListView.as_view(), name='faqs_list'),
    path('get-started/', views.GetStartedListView.as_view(), name='get_started_list'),
]