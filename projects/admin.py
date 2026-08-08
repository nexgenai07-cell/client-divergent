# projects/admin.py
from django.contrib import admin
from .models import ProjectSection, ProjectCard

@admin.register(ProjectSection)
class ProjectSectionAdmin(admin.ModelAdmin):
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

@admin.register(ProjectCard)
class ProjectCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'heading', 'project_section', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('project_section', 'is_active')
    search_fields = ('heading', 'description', 'technologies')
    ordering = ('project_section', 'order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('project_section', 'number', 'heading', 'description')
        }),
        ('Media', {
            'fields': ('icon', 'image')
        }),
        ('Content', {
            'fields': ('points', 'technologies', 'key_results')
        }),
        ('Order & Status', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['points'].help_text = 'Enter each point on a new line. Example:\n- Automated geometry\n- Optimization loops\n- Auto-generated reports'
        form.base_fields['technologies'].help_text = 'Enter each technology on a new line. Example:\n- Ansys HFSS\n- Python\n- Bayesian Optimization'
        form.base_fields['key_results'].help_text = 'Enter each result on a new line. Example:\n- 1.5 hours unattended run time\n- 90% reduction in manual setup'
        return form