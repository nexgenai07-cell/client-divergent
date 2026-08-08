# projects/models.py
from django.db import models
from website.models import BaseModel

class ProjectSection(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Project Section #{self.id}"

class ProjectCard(BaseModel):
    project_section = models.ForeignKey(ProjectSection, on_delete=models.CASCADE, related_name='projects')
    
    # Basic info
    number = models.CharField(max_length=10, blank=True, null=True, help_text="Card number/order (e.g., '01', '02')")
    heading = models.CharField(max_length=200, blank=True, null=True, help_text="Project title")
    description = models.TextField(blank=True, null=True, help_text="Project description")
    
    # Media
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="Font Awesome icon class (e.g., 'fas fa-microchip')")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Project image")
    
    # Content
    points = models.TextField(blank=True, null=True, help_text="Enter each point separated by newline")
    technologies = models.TextField(blank=True, null=True, help_text="Enter each technology separated by newline")
    key_results = models.TextField(blank=True, null=True, help_text="Enter each result separated by newline")
    
    # Order
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def get_points_list(self):
        """Return points as a list"""
        if self.points:
            return [p.strip() for p in self.points.split('\n') if p.strip()]
        return []
    
    def get_technologies_list(self):
        """Return technologies as a list"""
        if self.technologies:
            return [t.strip() for t in self.technologies.split('\n') if t.strip()]
        return []
    
    def get_key_results_list(self):
        """Return key results as a list"""
        if self.key_results:
            return [r.strip() for r in self.key_results.split('\n') if r.strip()]
        return []
    
    def __str__(self):
        return self.heading if self.heading else f"Project #{self.id}"