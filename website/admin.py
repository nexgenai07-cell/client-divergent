from django.contrib import admin
from .models import Page, Section, SectionItem, NavLink, SiteSettings, PricingPlan, Lead
from django.utils.html import format_html

class SectionItemInline(admin.TabularInline):
    model = SectionItem
    extra = 1


class PricingPlanInline(admin.TabularInline):
    model = PricingPlan
    extra = 1


class SectionInline(admin.StackedInline):
    model = Section
    extra = 1
    show_change_link = True


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'is_active', 'order')
    inlines = [SectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'page', 'section_type', 'order', 'is_active')
    list_filter = ('page', 'section_type', 'is_active')
    inlines = [SectionItemInline, PricingPlanInline]


@admin.register(SectionItem)
class SectionItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order', 'is_active')
    list_filter = ('section',)


@admin.register(NavLink)
class NavLinkAdmin(admin.ModelAdmin):
    list_display = ('label', 'location', 'link', 'order', 'is_active')
    list_filter = ('location',)


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'price', 'is_featured', 'order')


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'solver_used', 'created_at')
    readonly_fields = ('created_at',)





@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'logo_preview', 'calendar_link')
    fields = ('site_name', 'logo', 'logo_preview', 'calendar_link', 'copyright_text', 'social_links')
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height:50px;" />', obj.logo.url)
        return "No logo uploaded"
    logo_preview.short_description = "Logo Preview"

    def has_add_permission(self, request):
        return SiteSettings.objects.count() == 0

    def changelist_view(self, request, extra_context=None):
        # Since there's only ever one row, skip the list page and go straight to editing it
        obj = SiteSettings.load()
        from django.shortcuts import redirect
        return redirect(f'/admin/website/sitesettings/{obj.pk}/change/')