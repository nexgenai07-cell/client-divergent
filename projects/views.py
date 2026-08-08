# projects/views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import ProjectSection, ProjectCard
from .serializers import ProjectSectionSerializer, ProjectCardSerializer

# ============= VIEWSETS (CRUD Operations) =============
class ProjectSectionViewSet(viewsets.ModelViewSet):
    queryset = ProjectSection.objects.all()
    serializer_class = ProjectSectionSerializer
    permission_classes = [AllowAny]

class ProjectCardViewSet(viewsets.ModelViewSet):
    queryset = ProjectCard.objects.all()
    serializer_class = ProjectCardSerializer
    permission_classes = [AllowAny]

# ============= PUBLIC LIST VIEWS =============
class ProjectSectionListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectSectionSerializer
    queryset = ProjectSection.objects.filter(is_active=True)

class ProjectCardListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectCardSerializer
    queryset = ProjectCard.objects.filter(project_section__is_active=True, is_active=True).order_by('order')