# platform/serializers.py
from rest_framework import serializers
from .models import (
    PlatformSection, OperatingBenefit, WorkWithUs, ComingSoon,
    Demonstration, BuiltForProduction, PricingPlan
)

class OperatingBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingBenefit
        fields = [
            'id', 'heading', 'description', 'impact', 'icon', 'image',
            'order', 'is_active', 'created_at', 'updated_at'
        ]

class WorkWithUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkWithUs
        fields = [
            'id', 'heading', 'description', 'title', 'icon', 'image',
            'cta_label', 'cta_link', 'order', 'is_active', 'created_at', 'updated_at'
        ]

class ComingSoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComingSoon
        fields = [
            'id', 'heading', 'description', 'title', 'icon', 'image',
            'order', 'is_active', 'created_at', 'updated_at'
        ]

class DemonstrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demonstration
        fields = [
            'id', 'heading', 'description', 'video_url', 'video_thumbnail',
            'cta_label', 'cta_link', 'order', 'is_active', 'created_at', 'updated_at'
        ]

class BuiltForProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuiltForProduction
        fields = [
            'id', 'heading', 'description', 'icon', 'image',
            'order', 'is_active', 'created_at', 'updated_at'
        ]

class PricingPlanSerializer(serializers.ModelSerializer):
    included_list = serializers.SerializerMethodField()
    
    class Meta:
        model = PricingPlan
        fields = [
            'id', 'name', 'price', 'description', 'what_included', 'included_list',
            'best_for', 'cta_label', 'cta_link', 'is_featured',
            'order', 'is_active', 'created_at', 'updated_at'
        ]
    
    def get_included_list(self, obj):
        return obj.get_included_list()

class PlatformSectionSerializer(serializers.ModelSerializer):
    operating_benefits = OperatingBenefitSerializer(many=True, read_only=True)
    work_with_us = WorkWithUsSerializer(many=True, read_only=True)
    coming_soon = ComingSoonSerializer(many=True, read_only=True)
    demonstrations = DemonstrationSerializer(many=True, read_only=True)
    built_for_production = BuiltForProductionSerializer(many=True, read_only=True)
    pricing_plans = PricingPlanSerializer(many=True, read_only=True)
    
    class Meta:
        model = PlatformSection
        fields = [
            'id', 'heading', 'description', 'is_active',
            'operating_benefits', 'work_with_us', 'coming_soon',
            'demonstrations', 'built_for_production', 'pricing_plans',
            'created_at', 'updated_at'
        ]