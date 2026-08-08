from rest_framework import serializers
from .models import Page, Section, SectionItem, NavLink, SiteSettings, PricingPlan, Lead


class SectionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionItem
        fields = [
            'id', 'title', 'description', 'name', 'role',
            'image', 'link', 'order', 'extra_data',
        ]


class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = [
            'id', 'name', 'price', 'description', 'features',
            'button_text', 'button_link', 'is_featured', 'order',
        ]


class SectionSerializer(serializers.ModelSerializer):
    items = SectionItemSerializer(many=True, read_only=True)
    pricing_plans = PricingPlanSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = [
            'id', 'page', 'section_type', 'name', 'heading', 'subheading',
            'button_text', 'button_link', 'image', 'video_url',
            'extra_data', 'order', 'items', 'pricing_plans',
        ]


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'name', 'title', 'meta_description', 'order']


class PageDetailSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['id', 'name', 'title', 'meta_description', 'order', 'sections']


class NavLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavLink
        fields = ['id', 'label', 'link', 'location', 'order']


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ['site_name', 'logo', 'calendar_link', 'copyright_text', 'social_links']


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'company_name', 'email', 'solver_used', 'workflow_description', 'created_at']
        read_only_fields = ['id', 'created_at']