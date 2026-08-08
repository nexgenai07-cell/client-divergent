from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Page, Section, SectionItem, NavLink, SiteSettings, PricingPlan, Lead
from .serializers import (
    PageSerializer, PageDetailSerializer, SectionSerializer, SectionItemSerializer,
    NavLinkSerializer, SiteSettingsSerializer, PricingPlanSerializer, LeadSerializer
)


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.filter(is_active=True)
    serializer_class = PageSerializer
    lookup_field = 'name'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PageDetailSerializer
        return PageSerializer


class SectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Section.objects.filter(is_active=True)
    serializer_class = SectionSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        page = self.request.query_params.get('page')
        if page:
            qs = qs.filter(page__name=page)
        return qs


class SectionItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SectionItem.objects.filter(is_active=True)
    serializer_class = SectionItemSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        section = self.request.query_params.get('section')
        if section:
            qs = qs.filter(section_id=section)
        return qs


class NavLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NavLink.objects.filter(is_active=True)
    serializer_class = NavLinkSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        location = self.request.query_params.get('location')
        if location:
            qs = qs.filter(location=location)
        return qs


class PricingPlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PricingPlan.objects.filter(is_active=True)
    serializer_class = PricingPlanSerializer


class LeadViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class SiteSettingsView(APIView):
    def get(self, request):
        settings_obj = SiteSettings.load()
        serializer = SiteSettingsSerializer(settings_obj, context={'request': request})
        return Response(serializer.data)