# about/models.py
from django.db import models
from website.models import BaseModel

class AboutSection(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"About Section #{self.id}"

class TeamMember(BaseModel):
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='team_members')
    
    # Personal Info
    name = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True, help_text="e.g., PhD, RF Engineer")
    role = models.CharField(max_length=200, blank=True, null=True, help_text="e.g., Co-Founder, Lead Engineer")
    description = models.TextField(blank=True, null=True, help_text="Team member bio/description")
    
    # Media
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    
    # Social Links
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    # Order
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name if self.name else f"Team Member #{self.id}"

class Publication(BaseModel):
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='publications')
    
    title = models.CharField(max_length=500, blank=True, null=True)
    authors = models.CharField(max_length=500, blank=True, null=True)
    journal = models.CharField(max_length=200, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    citation = models.TextField(blank=True, null=True, help_text="Full citation in APA/MLA format")
    
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title[:50] if self.title else f"Publication #{self.id}"

class Patent(BaseModel):
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='patents')
    
    title = models.CharField(max_length=500, blank=True, null=True)
    patent_number = models.CharField(max_length=100, blank=True, null=True)
    inventors = models.CharField(max_length=500, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title[:50] if self.title else f"Patent #{self.id}"

class AboutStat(BaseModel):
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='stats')
    
    label = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="Font Awesome icon class")
    
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.value} {self.label}" if self.value and self.label else f"Stat #{self.id}"