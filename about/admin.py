# about/admin.py
from django.contrib import admin
from .models import AboutSection, TeamMember, Publication, Patent, AboutStat

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
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

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'designation', 'about_section', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('about_section', 'is_active', 'role')
    search_fields = ('name', 'role', 'designation', 'description')
    ordering = ('about_section', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('about_section', 'name', 'designation', 'role', 'description')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Social Links', {
            'fields': ('linkedin', 'github', 'twitter', 'website'),
            'classes': ('collapse',)
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'journal', 'year', 'about_section', 'is_active', 'created_at')
    list_editable = ('is_active',)
    list_filter = ('about_section', 'is_active', 'year')
    search_fields = ('title', 'authors', 'journal')
    ordering = ('about_section', '-year', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Publication Details', {
            'fields': ('about_section', 'title', 'authors', 'journal', 'year', 'link', 'citation')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'patent_number', 'year', 'about_section', 'is_active', 'created_at')
    list_editable = ('is_active',)
    list_filter = ('about_section', 'is_active', 'year')
    search_fields = ('title', 'patent_number', 'inventors')
    ordering = ('about_section', '-year', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Patent Details', {
            'fields': ('about_section', 'title', 'patent_number', 'inventors', 'year', 'link')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(AboutStat)
class AboutStatAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'value', 'icon', 'about_section', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('about_section', 'is_active')
    search_fields = ('label', 'value')
    ordering = ('about_section', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Stat Details', {
            'fields': ('about_section', 'label', 'value', 'icon')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )