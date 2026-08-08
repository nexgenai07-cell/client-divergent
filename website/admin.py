# website/admin.py
from django.contrib import admin
from .models import *

class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(HeroSection)
class HeroSectionAdmin(BaseAdmin):
    list_display = ('id', 'title', 'is_active', 'order', 'created_at')
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'subtitle')
    ordering = ('order',)
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'description', 'built_by', 'call_to_action_1', 'call_to_action_2')
        }),
        ('Status', {
            'fields': ('is_active', 'order', 'created_at', 'updated_at')
        }),
    )

@admin.register(PipelineStep)
class PipelineStepAdmin(BaseAdmin):
    list_display = ('id', 'step_name', 'hero_section', 'order', 'created_at')
    list_editable = ('order',)
    list_filter = ('hero_section',)
    search_fields = ('step_name', 'description')
    ordering = ('hero_section', 'order')

@admin.register(ProblemStatement)
class ProblemStatementAdmin(BaseAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)

@admin.register(ProblemQuote)
class ProblemQuoteAdmin(BaseAdmin):
    list_display = ('id', 'author', 'author_title', 'problem_statement', 'order', 'created_at')
    list_editable = ('order',)
    list_filter = ('problem_statement',)
    search_fields = ('author', 'quote_text')
    ordering = ('problem_statement', 'order')

@admin.register(Statistic)
class StatisticAdmin(BaseAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)

@admin.register(StatItem)
class StatItemAdmin(BaseAdmin):
    list_display = ('id', 'value', 'label', 'statistic', 'order', 'created_at')
    list_editable = ('order',)
    list_filter = ('statistic',)
    search_fields = ('value', 'label')
    ordering = ('statistic', 'order')

@admin.register(FieldNote)
class FieldNoteAdmin(BaseAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)

@admin.register(FieldNoteItem)
class FieldNoteItemAdmin(BaseAdmin):
    list_display = ('id', 'author', 'author_title', 'field_note', 'order', 'created_at')
    list_editable = ('order',)
    list_filter = ('field_note',)
    search_fields = ('author', 'quote')
    ordering = ('field_note', 'order')

@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)
    search_fields = ('heading', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Section Content', {
            'fields': ('heading', 'description')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ServiceCard)
class ServiceCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'service_section', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('service_section', 'is_active')
    search_fields = ('heading', 'description', 'points')
    ordering = ('service_section', 'order')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Card Content', {
            'fields': ('service_section', 'heading', 'description', 'icon', 'image', 'points')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(CaseStudy)
class CaseStudyAdmin(BaseAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)

@admin.register(CaseStudyCard)
class CaseStudyCardAdmin(BaseAdmin):
    list_display = ('id', 'title', 'case_study', 'order', 'created_at')
    list_editable = ('order',)
    list_filter = ('case_study',)
    search_fields = ('title', 'description')
    ordering = ('case_study', 'order')

@admin.register(AssetSection)
class AssetSectionAdmin(BaseAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)

@admin.register(AssetItem)
class AssetItemAdmin(BaseAdmin):
    list_display = ('id', 'title', 'asset_section', 'order', 'created_at')
    list_editable = ('order',)
    list_filter = ('asset_section',)
    search_fields = ('title', 'description')
    ordering = ('asset_section', 'order')

@admin.register(HowWeWork)
class HowWeWorkAdmin(BaseAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)

@admin.register(HowWeWorkStep)
class HowWeWorkStepAdmin(BaseAdmin):
    list_display = ('id', 'step_number', 'title', 'how_we_work', 'order', 'created_at')
    list_editable = ('order',)
    list_filter = ('how_we_work',)
    search_fields = ('title', 'description')
    ordering = ('how_we_work', 'order')

@admin.register(WhyUsSection)
class WhyUsSectionAdmin(BaseAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)

@admin.register(WhyUsCard)
class WhyUsCardAdmin(BaseAdmin):
    list_display = ('id', 'number', 'title', 'why_us_section', 'order', 'created_at')
    list_editable = ('order',)
    list_filter = ('why_us_section',)
    search_fields = ('title', 'description')
    ordering = ('why_us_section', 'order')

@admin.register(OurPlatform)
class OurPlatformAdmin(BaseAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)

@admin.register(PlatformFeature)
class PlatformFeatureAdmin(BaseAdmin):
    list_display = ('id', 'title', 'platform', 'order', 'created_at')
    list_editable = ('order',)
    list_filter = ('platform',)
    search_fields = ('title', 'description')
    ordering = ('platform', 'order')

@admin.register(FAQ)
class FAQAdmin(BaseAdmin):
    list_display = ('id', 'question', 'is_active', 'order', 'created_at')
    list_editable = ('is_active', 'order')
    search_fields = ('question', 'answer')

@admin.register(GetStartedSection)
class GetStartedSectionAdmin(BaseAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)