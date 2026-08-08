# platform/views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *

# ============= VIEWSETS (CRUD Operations) =============
class PlatformSectionViewSet(viewsets.ModelViewSet):
    queryset = PlatformSection.objects.all()
    serializer_class = PlatformSectionSerializer
    permission_classes = [AllowAny]

class OperatingBenefitViewSet(viewsets.ModelViewSet):
    queryset = OperatingBenefit.objects.all()
    serializer_class = OperatingBenefitSerializer
    permission_classes = [AllowAny]

class WorkWithUsViewSet(viewsets.ModelViewSet):
    queryset = WorkWithUs.objects.all()
    serializer_class = WorkWithUsSerializer
    permission_classes = [AllowAny]

class ComingSoonViewSet(viewsets.ModelViewSet):
    queryset = ComingSoon.objects.all()
    serializer_class = ComingSoonSerializer
    permission_classes = [AllowAny]

class DemonstrationViewSet(viewsets.ModelViewSet):
    queryset = Demonstration.objects.all()
    serializer_class = DemonstrationSerializer
    permission_classes = [AllowAny]

class BuiltForProductionViewSet(viewsets.ModelViewSet):
    queryset = BuiltForProduction.objects.all()
    serializer_class = BuiltForProductionSerializer
    permission_classes = [AllowAny]

class PricingPlanViewSet(viewsets.ModelViewSet):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer
    permission_classes = [AllowAny]

# ============= PUBLIC LIST VIEWS =============
class PlatformSectionListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlatformSectionSerializer
    queryset = PlatformSection.objects.filter(is_active=True)

class OperatingBenefitListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = OperatingBenefitSerializer
    queryset = OperatingBenefit.objects.filter(platform_section__is_active=True, is_active=True).order_by('order')

class WorkWithUsListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = WorkWithUsSerializer
    queryset = WorkWithUs.objects.filter(platform_section__is_active=True, is_active=True).order_by('order')

class ComingSoonListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ComingSoonSerializer
    queryset = ComingSoon.objects.filter(platform_section__is_active=True, is_active=True).order_by('order')

class DemonstrationListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = DemonstrationSerializer
    queryset = Demonstration.objects.filter(platform_section__is_active=True, is_active=True).order_by('order')

class BuiltForProductionListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BuiltForProductionSerializer
    queryset = BuiltForProduction.objects.filter(platform_section__is_active=True, is_active=True).order_by('order')

class PricingPlanListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PricingPlanSerializer
    queryset = PricingPlan.objects.filter(platform_section__is_active=True, is_active=True).order_by('order')