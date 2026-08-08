# website/views.py
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from projects.models import ProjectSection
from .models import *
from .serializers import *
from projects.serializers import ProjectSectionSerializer
# website/views.py - Add import and update WebsiteDataView
from about.models import AboutSection
from about.serializers import AboutSectionSerializer
# ============= VIEWSETS (CRUD Operations) =============
class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    permission_classes = [AllowAny]

class PipelineStepViewSet(viewsets.ModelViewSet):
    queryset = PipelineStep.objects.all()
    serializer_class = PipelineStepSerializer
    permission_classes = [AllowAny]

class ProblemStatementViewSet(viewsets.ModelViewSet):
    queryset = ProblemStatement.objects.all()
    serializer_class = ProblemStatementSerializer
    permission_classes = [AllowAny]

class ProblemQuoteViewSet(viewsets.ModelViewSet):
    queryset = ProblemQuote.objects.all()
    serializer_class = ProblemQuoteSerializer
    permission_classes = [AllowAny]

class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    permission_classes = [AllowAny]

class StatItemViewSet(viewsets.ModelViewSet):
    queryset = StatItem.objects.all()
    serializer_class = StatItemSerializer
    permission_classes = [AllowAny]

class FieldNoteViewSet(viewsets.ModelViewSet):
    queryset = FieldNote.objects.all()
    serializer_class = FieldNoteSerializer
    permission_classes = [AllowAny]

class FieldNoteItemViewSet(viewsets.ModelViewSet):
    queryset = FieldNoteItem.objects.all()
    serializer_class = FieldNoteItemSerializer
    permission_classes = [AllowAny]

class ServiceSectionViewSet(viewsets.ModelViewSet):
    queryset = ServiceSection.objects.all()
    serializer_class = ServiceSectionSerializer
    permission_classes = [AllowAny]

class ServiceCardViewSet(viewsets.ModelViewSet):
    queryset = ServiceCard.objects.all()
    serializer_class = ServiceCardSerializer
    permission_classes = [AllowAny]

class CaseStudyViewSet(viewsets.ModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    permission_classes = [AllowAny]

class CaseStudyCardViewSet(viewsets.ModelViewSet):
    queryset = CaseStudyCard.objects.all()
    serializer_class = CaseStudyCardSerializer
    permission_classes = [AllowAny]

class AssetSectionViewSet(viewsets.ModelViewSet):
    queryset = AssetSection.objects.all()
    serializer_class = AssetSectionSerializer
    permission_classes = [AllowAny]

class AssetItemViewSet(viewsets.ModelViewSet):
    queryset = AssetItem.objects.all()
    serializer_class = AssetItemSerializer
    permission_classes = [AllowAny]

class HowWeWorkViewSet(viewsets.ModelViewSet):
    queryset = HowWeWork.objects.all()
    serializer_class = HowWeWorkSerializer
    permission_classes = [AllowAny]

class HowWeWorkStepViewSet(viewsets.ModelViewSet):
    queryset = HowWeWorkStep.objects.all()
    serializer_class = HowWeWorkStepSerializer
    permission_classes = [AllowAny]

class WhyUsSectionViewSet(viewsets.ModelViewSet):
    queryset = WhyUsSection.objects.all()
    serializer_class = WhyUsSectionSerializer
    permission_classes = [AllowAny]

class WhyUsCardViewSet(viewsets.ModelViewSet):
    queryset = WhyUsCard.objects.all()
    serializer_class = WhyUsCardSerializer
    permission_classes = [AllowAny]

class OurPlatformViewSet(viewsets.ModelViewSet):
    queryset = OurPlatform.objects.all()
    serializer_class = OurPlatformSerializer
    permission_classes = [AllowAny]

class PlatformFeatureViewSet(viewsets.ModelViewSet):
    queryset = PlatformFeature.objects.all()
    serializer_class = PlatformFeatureSerializer
    permission_classes = [AllowAny]

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [AllowAny]

class GetStartedSectionViewSet(viewsets.ModelViewSet):
    queryset = GetStartedSection.objects.all()
    serializer_class = GetStartedSectionSerializer
    permission_classes = [AllowAny]

# ============= COMBINED DATA VIEW =============


class WebsiteDataView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        hero = HeroSection.objects.filter(is_active=True).first()
        pipeline_steps = PipelineStep.objects.filter(hero_section=hero).order_by('order') if hero else []
        
        problem_statement = ProblemStatement.objects.filter(is_active=True).first()
        statistic = Statistic.objects.filter(is_active=True).first()
        field_note = FieldNote.objects.filter(is_active=True).first()
        service_section = ServiceSection.objects.filter(is_active=True).first()
        case_study = CaseStudy.objects.filter(is_active=True).first()
        asset_section = AssetSection.objects.filter(is_active=True).first()
        how_we_work = HowWeWork.objects.filter(is_active=True).first()
        why_us = WhyUsSection.objects.filter(is_active=True).first()
        platform = OurPlatform.objects.filter(is_active=True).first()
        faqs = FAQ.objects.filter(is_active=True).order_by('order')
        get_started = GetStartedSection.objects.filter(is_active=True).first()
        
        project_section = ProjectSection.objects.filter(is_active=True).first()
        about_section = AboutSection.objects.filter(is_active=True).first()
        
        data = {
            'hero': HeroSectionSerializer(hero).data if hero else None,
            'pipeline_steps': PipelineStepSerializer(pipeline_steps, many=True).data,
            'problem_statement': ProblemStatementSerializer(problem_statement).data if problem_statement else None,
            'statistic': StatisticSerializer(statistic).data if statistic else None,
            'field_note': FieldNoteSerializer(field_note).data if field_note else None,
            'service_section': ServiceSectionSerializer(service_section).data if service_section else None,
            'case_study': CaseStudySerializer(case_study).data if case_study else None,
            'asset_section': AssetSectionSerializer(asset_section).data if asset_section else None,
            'how_we_work': HowWeWorkSerializer(how_we_work).data if how_we_work else None,
            'why_us': WhyUsSectionSerializer(why_us).data if why_us else None,
            'platform': OurPlatformSerializer(platform).data if platform else None,
            'faqs': FAQSerializer(faqs, many=True).data,
            'get_started': GetStartedSectionSerializer(get_started).data if get_started else None,
            'projects': ProjectSectionSerializer(project_section).data if project_section else None,
            'about': AboutSectionSerializer(about_section).data if about_section else None,
        }
        
        return Response(data)
# ============= INDIVIDUAL LIST VIEWS (Public) =============
class HeroListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = HeroSectionSerializer
    queryset = HeroSection.objects.filter(is_active=True)

class PipelineStepListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PipelineStepSerializer
    queryset = PipelineStep.objects.filter(hero_section__is_active=True).order_by('order')

class ProblemStatementListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProblemStatementSerializer
    queryset = ProblemStatement.objects.filter(is_active=True)

class ProblemQuoteListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProblemQuoteSerializer
    queryset = ProblemQuote.objects.filter(problem_statement__is_active=True).order_by('order')

class StatisticsListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = StatisticSerializer
    queryset = Statistic.objects.filter(is_active=True)

class StatItemListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = StatItemSerializer
    queryset = StatItem.objects.filter(statistic__is_active=True).order_by('order')

class FieldNoteListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FieldNoteSerializer
    queryset = FieldNote.objects.filter(is_active=True)

class FieldNoteItemListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FieldNoteItemSerializer
    queryset = FieldNoteItem.objects.filter(field_note__is_active=True).order_by('order')

class ServiceSectionListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ServiceSectionSerializer
    queryset = ServiceSection.objects.filter(is_active=True)

class ServiceCardListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ServiceCardSerializer
    queryset = ServiceCard.objects.filter(service_section__is_active=True, is_active=True).order_by('order')

class CaseStudyListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CaseStudySerializer
    queryset = CaseStudy.objects.filter(is_active=True)

class CaseStudyCardListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CaseStudyCardSerializer
    queryset = CaseStudyCard.objects.filter(case_study__is_active=True).order_by('order')

class AssetSectionListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AssetSectionSerializer
    queryset = AssetSection.objects.filter(is_active=True)

class AssetItemListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AssetItemSerializer
    queryset = AssetItem.objects.filter(asset_section__is_active=True).order_by('order')

class HowWeWorkListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = HowWeWorkSerializer
    queryset = HowWeWork.objects.filter(is_active=True)

class HowWeWorkStepListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = HowWeWorkStepSerializer
    queryset = HowWeWorkStep.objects.filter(how_we_work__is_active=True).order_by('order')

class WhyUsSectionListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = WhyUsSectionSerializer
    queryset = WhyUsSection.objects.filter(is_active=True)

class WhyUsCardListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = WhyUsCardSerializer
    queryset = WhyUsCard.objects.filter(why_us_section__is_active=True).order_by('order')

class PlatformListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = OurPlatformSerializer
    queryset = OurPlatform.objects.filter(is_active=True)

class PlatformFeatureListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlatformFeatureSerializer
    queryset = PlatformFeature.objects.filter(platform__is_active=True).order_by('order')

class FAQListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FAQSerializer
    queryset = FAQ.objects.filter(is_active=True).order_by('order')

class GetStartedListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GetStartedSectionSerializer
    queryset = GetStartedSection.objects.filter(is_active=True)