# platform/models.py
from django.db import models
from website.models import BaseModel

class PlatformSection(BaseModel):
    """Main platform section"""
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Platform Section #{self.id}"

# ============= OPERATING BENEFITS =============
class OperatingBenefit(BaseModel):
    platform_section = models.ForeignKey(PlatformSection, on_delete=models.CASCADE, related_name='operating_benefits')
    
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    impact = models.CharField(max_length=200, blank=True, null=True, help_text="Impact statement (e.g., 'Faster evaluation of design alternatives')")
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="Font Awesome icon class")
    image = models.ImageField(upload_to='platform/benefits/', blank=True, null=True)
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Operating Benefit #{self.id}"

# ============= WORK WITH US =============
class WorkWithUs(BaseModel):
    platform_section = models.ForeignKey(PlatformSection, on_delete=models.CASCADE, related_name='work_with_us')
    
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True, help_text="Card title (e.g., 'Agents', 'Services')")
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="Font Awesome icon class")
    image = models.ImageField(upload_to='platform/work/', blank=True, null=True)
    cta_label = models.CharField(max_length=100, blank=True, null=True, help_text="Call to action label")
    cta_link = models.URLField(blank=True, null=True, help_text="Call to action link")
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title if self.title else f"Work With Us #{self.id}"

# ============= COMING SOON =============
class ComingSoon(BaseModel):
    platform_section = models.ForeignKey(PlatformSection, on_delete=models.CASCADE, related_name='coming_soon')
    
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="Font Awesome icon class")
    image = models.ImageField(upload_to='platform/coming-soon/', blank=True, null=True)
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title if self.title else f"Coming Soon #{self.id}"

# ============= DEMONSTRATION =============
class Demonstration(BaseModel):
    platform_section = models.ForeignKey(PlatformSection, on_delete=models.CASCADE, related_name='demonstrations')
    
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube or Vimeo URL")
    video_thumbnail = models.ImageField(upload_to='platform/demos/', blank=True, null=True)
    cta_label = models.CharField(max_length=100, blank=True, null=True)
    cta_link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Demonstration #{self.id}"

# ============= BUILT FOR PRODUCTION =============
class BuiltForProduction(BaseModel):
    platform_section = models.ForeignKey(PlatformSection, on_delete=models.CASCADE, related_name='built_for_production')
    
    heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="Font Awesome icon class")
    image = models.ImageField(upload_to='platform/production/', blank=True, null=True)
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.heading if self.heading else f"Built For Production #{self.id}"

# ============= PRICING PLANS =============
class PricingPlan(BaseModel):
    platform_section = models.ForeignKey(PlatformSection, on_delete=models.CASCADE, related_name='pricing_plans')
    
    name = models.CharField(max_length=100, blank=True, null=True, help_text="Plan name (e.g., 'Professional', 'Enterprise')")
    price = models.CharField(max_length=50, blank=True, null=True, help_text="Price (e.g., '$400 PER MONTH', 'Custom Pricing')")
    description = models.TextField(blank=True, null=True)
    what_included = models.TextField(blank=True, null=True, help_text="Enter each included feature separated by newline")
    best_for = models.CharField(max_length=200, blank=True, null=True, help_text="Best for (e.g., 'Individuals & Small Teams')")
    cta_label = models.CharField(max_length=100, blank=True, null=True)
    cta_link = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Highlight as featured plan")
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def get_included_list(self):
        """Return included features as a list"""
        if self.what_included:
            return [item.strip() for item in self.what_included.split('\n') if item.strip()]
        return []
    
    def __str__(self):
        return self.name if self.name else f"Pricing Plan #{self.id}"