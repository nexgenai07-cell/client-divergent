# about/views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import AboutSection, TeamMember, Publication, Patent, AboutStat
from .serializers import (
    AboutSectionSerializer, 
    TeamMemberSerializer, 
    PublicationSerializer, 
    PatentSerializer, 
    AboutStatSerializer
)

# ============= VIEWSETS (CRUD Operations) =============
class AboutSectionViewSet(viewsets.ModelViewSet):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer
    permission_classes = [AllowAny]

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = [AllowAny]

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [AllowAny]

class PatentViewSet(viewsets.ModelViewSet):
    queryset = Patent.objects.all()
    serializer_class = PatentSerializer
    permission_classes = [AllowAny]

class AboutStatViewSet(viewsets.ModelViewSet):
    queryset = AboutStat.objects.all()
    serializer_class = AboutStatSerializer
    permission_classes = [AllowAny]

# ============= PUBLIC LIST VIEWS =============
class AboutSectionListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AboutSectionSerializer
    queryset = AboutSection.objects.filter(is_active=True)

class TeamMemberListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.filter(about_section__is_active=True, is_active=True).order_by('order')

class PublicationListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PublicationSerializer
    queryset = Publication.objects.filter(about_section__is_active=True, is_active=True).order_by('-year', 'order')

class PatentListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PatentSerializer
    queryset = Patent.objects.filter(about_section__is_active=True, is_active=True).order_by('-year', 'order')

class AboutStatListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AboutStatSerializer
    queryset = AboutStat.objects.filter(about_section__is_active=True, is_active=True).order_by('order')