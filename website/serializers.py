# website/serializers.py
from rest_framework import serializers
from .models import *

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class PipelineStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PipelineStep
        fields = '__all__'

class ProblemQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemQuote
        fields = '__all__'

class ProblemStatementSerializer(serializers.ModelSerializer):
    quotes = ProblemQuoteSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProblemStatement
        fields = '__all__'

class StatItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatItem
        fields = '__all__'

class StatisticSerializer(serializers.ModelSerializer):
    stats = StatItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Statistic
        fields = '__all__'

class FieldNoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldNoteItem
        fields = '__all__'

class FieldNoteSerializer(serializers.ModelSerializer):
    notes = FieldNoteItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = FieldNote
        fields = '__all__'

class ServiceCardSerializer(serializers.ModelSerializer):
    points_list = serializers.SerializerMethodField()
    
    class Meta:
        model = ServiceCard
        fields = [
            'id', 
            'heading', 
            'description', 
            'icon', 
            'image', 
            'points',
            'points_list',
            'order',
            'is_active',
            'created_at',
            'updated_at'
        ]
    
    def get_points_list(self, obj):
        return obj.get_points_list()

class ServiceSectionSerializer(serializers.ModelSerializer):
    services = ServiceCardSerializer(many=True, read_only=True)
    
    class Meta:
        model = ServiceSection
        fields = ['id', 'heading', 'description', 'is_active', 'services', 'created_at', 'updated_at']

class CaseStudyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudyCard
        fields = '__all__'

class CaseStudySerializer(serializers.ModelSerializer):
    cards = CaseStudyCardSerializer(many=True, read_only=True)
    
    class Meta:
        model = CaseStudy
        fields = '__all__'

class AssetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetItem
        fields = '__all__'

class AssetSectionSerializer(serializers.ModelSerializer):
    assets = AssetItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = AssetSection
        fields = '__all__'

class HowWeWorkStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWeWorkStep
        fields = '__all__'

class HowWeWorkSerializer(serializers.ModelSerializer):
    steps = HowWeWorkStepSerializer(many=True, read_only=True)
    
    class Meta:
        model = HowWeWork
        fields = '__all__'

class WhyUsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUsCard
        fields = '__all__'

class WhyUsSectionSerializer(serializers.ModelSerializer):
    cards = WhyUsCardSerializer(many=True, read_only=True)
    
    class Meta:
        model = WhyUsSection
        fields = '__all__'

class PlatformFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformFeature
        fields = '__all__'

class OurPlatformSerializer(serializers.ModelSerializer):
    features = PlatformFeatureSerializer(many=True, read_only=True)
    
    class Meta:
        model = OurPlatform
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class GetStartedSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetStartedSection
        fields = '__all__'