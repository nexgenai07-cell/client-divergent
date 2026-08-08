# website/models.py
from django.db import models
from django.utils.text import slugify

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class HeroSection(BaseModel):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    built_by = models.TextField(blank=True, null=True)
    call_to_action_1 = models.CharField(max_length=100, blank=True, null=True)
    call_to_action_2 = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title if self.title else f"Hero #{self.id}"

class PipelineStep(BaseModel):
    hero_section = models.ForeignKey(HeroSection, on_delete=models.CASCADE, related_name='pipeline_steps')
    step_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.step_name if self.step_name else f"Step #{self.id}"

class ProblemStatement(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    sub_heading = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Problem #{self.id}"

class ProblemQuote(BaseModel):
    problem_statement = models.ForeignKey(ProblemStatement, on_delete=models.CASCADE, related_name='quotes')
    quote_text = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    author_title = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.author if self.author else f"Quote #{self.id}"

class Statistic(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    sub_heading = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Stats #{self.id}"

class StatItem(BaseModel):
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE, related_name='stats')
    value = models.CharField(max_length=50, blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.value if self.value else f"Stat #{self.id}"

class FieldNote(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    sub_heading = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Field Note #{self.id}"

class FieldNoteItem(BaseModel):
    field_note = models.ForeignKey(FieldNote, on_delete=models.CASCADE, related_name='notes')
    quote = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    author_title = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.author if self.author else f"Note #{self.id}"

class ServiceSection(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Service Section #{self.id}"

class ServiceCard(BaseModel):
    service_section = models.ForeignKey(ServiceSection, on_delete=models.CASCADE, related_name='services')
    heading = models.CharField(max_length=200, blank=True, null=True, help_text="Card heading/title")
    description = models.TextField(blank=True, null=True, help_text="Card main description")
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="Font Awesome icon class (e.g., 'fas fa-robot')")
    image = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Card image (optional)")
    points = models.TextField(blank=True, null=True, help_text="Enter each point separated by newline")
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def get_points_list(self):
        """Return points as a list"""
        if self.points:
            return [p.strip() for p in self.points.split('\n') if p.strip()]
        return []
    
    def __str__(self):
        return self.heading if self.heading else f"Service Card #{self.id}"

class CaseStudy(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Case Study #{self.id}"

class CaseStudyCard(BaseModel):
    case_study = models.ForeignKey(CaseStudy, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='case_studies/', blank=True, null=True)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title if self.title else f"Case Card #{self.id}"

class AssetSection(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Asset #{self.id}"

class AssetItem(BaseModel):
    asset_section = models.ForeignKey(AssetSection, on_delete=models.CASCADE, related_name='assets')
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='assets/', blank=True, null=True)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title if self.title else f"Asset Item #{self.id}"

class HowWeWork(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"How We Work #{self.id}"

class HowWeWorkStep(BaseModel):
    how_we_work = models.ForeignKey(HowWeWork, on_delete=models.CASCADE, related_name='steps')
    step_number = models.IntegerField(default=0)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='steps/', blank=True, null=True)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return f"Step {self.step_number}: {self.title if self.title else ''}"

class WhyUsSection(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Why Us #{self.id}"

class WhyUsCard(BaseModel):
    why_us_section = models.ForeignKey(WhyUsSection, on_delete=models.CASCADE, related_name='cards')
    number = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title if self.title else f"Why Us Card #{self.id}"

class OurPlatform(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Platform #{self.id}"

class PlatformFeature(BaseModel):
    platform = models.ForeignKey(OurPlatform, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='platform/', blank=True, null=True)
    order = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title if self.title else f"Feature #{self.id}"

class FAQ(BaseModel):
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.question[:50] if self.question else f"FAQ #{self.id}"

class GetStartedSection(BaseModel):
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='get_started/', blank=True, null=True)
    call_to_action = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Get Started #{self.id}"