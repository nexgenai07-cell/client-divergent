# platform/admin.py
from django.contrib import admin
from .models import *

@admin.register(PlatformSection)
class PlatformSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'is_active', 'created_at')
    list_editable = ('is_active',)
    search_fields = ('heading', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(OperatingBenefit)
class OperatingBenefitAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'impact', 'platform_section', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('platform_section', 'is_active')
    search_fields = ('heading', 'description', 'impact')
    ordering = ('platform_section', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Benefit Content', {
            'fields': ('platform_section', 'heading', 'description', 'impact')
        }),
        ('Media', {
            'fields': ('icon', 'image')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(WorkWithUs)
class WorkWithUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'platform_section', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('platform_section', 'is_active')
    search_fields = ('title', 'heading', 'description')
    ordering = ('platform_section', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Content', {
            'fields': ('platform_section', 'heading', 'description', 'title')
        }),
        ('Media & CTA', {
            'fields': ('icon', 'image', 'cta_label', 'cta_link')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ComingSoon)
class ComingSoonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'platform_section', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('platform_section', 'is_active')
    search_fields = ('title', 'heading', 'description')
    ordering = ('platform_section', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Content', {
            'fields': ('platform_section', 'heading', 'description', 'title')
        }),
        ('Media', {
            'fields': ('icon', 'image')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Demonstration)
class DemonstrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'platform_section', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('platform_section', 'is_active')
    search_fields = ('heading', 'description')
    ordering = ('platform_section', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Content', {
            'fields': ('platform_section', 'heading', 'description')
        }),
        ('Video', {
            'fields': ('video_url', 'video_thumbnail')
        }),
        ('CTA', {
            'fields': ('cta_label', 'cta_link')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(BuiltForProduction)
class BuiltForProductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'platform_section', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('platform_section', 'is_active')
    search_fields = ('heading', 'description')
    ordering = ('platform_section', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Content', {
            'fields': ('platform_section', 'heading', 'description')
        }),
        ('Media', {
            'fields': ('icon', 'image')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_featured', 'platform_section', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active', 'is_featured')
    list_filter = ('platform_section', 'is_active', 'is_featured')
    search_fields = ('name', 'description', 'best_for')
    ordering = ('platform_section', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Plan Details', {
            'fields': ('platform_section', 'name', 'price', 'description', 'best_for')
        }),
        ('What\'s Included', {
            'fields': ('what_included',)
        }),
        ('CTA', {
            'fields': ('cta_label', 'cta_link')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['what_included'].help_text = 'Enter each feature on a new line. Example:\n- Feature 1\n- Feature 2\n- Feature 3'
        return form