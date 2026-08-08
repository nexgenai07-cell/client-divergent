from django.db import models


class Page(models.Model):
    name = models.SlugField(unique=True)  # home, wireless, about, platform
    title = models.CharField(max_length=255)
    meta_description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Section(models.Model):
    SECTION_TYPES = [
        ('hero', 'Hero'),
        ('problem', 'Problem Framing'),
        ('stats', 'Stats'),
        ('field_notes', 'Field Notes'),
        ('services', 'Services'),
        ('case_study', 'Case Study'),
        ('assets', 'Assets'),
        ('how_we_work', 'How We Work'),
        ('why_us', 'Why Us'),
        ('demo', 'Demonstration'),
        ('faq', 'FAQ'),
        ('cta', 'CTA'),
        ('about', 'About / Team'),
        ('logos', 'Company Logos'),
        ('custom', 'Custom'),
    ]

    page = models.ForeignKey(Page, related_name='sections', on_delete=models.CASCADE)
    section_type = models.CharField(max_length=30, choices=SECTION_TYPES)
    name = models.CharField(max_length=255)  # dynamic display label
    heading = models.CharField(max_length=500, blank=True)
    subheading = models.TextField(blank=True)
    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='sections/', blank=True, null=True)
    video_url = models.URLField(blank=True)
    extra_data = models.JSONField(blank=True, null=True, default=dict)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.page.name} - {self.name}"


class SectionItem(models.Model):
    section = models.ForeignKey(Section, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    name = models.CharField(max_length=255, blank=True)   # person name (testimonials/team)
    role = models.CharField(max_length=255, blank=True)   # person role/title
    image = models.ImageField(upload_to='section_items/', blank=True, null=True)
    link = models.CharField(max_length=500, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    extra_data = models.JSONField(blank=True, null=True, default=dict)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or self.name or f"Item {self.pk}"


class NavLink(models.Model):
    LOCATION_CHOICES = [('nav', 'Navigation'), ('footer', 'Footer')]

    label = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default='nav')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_location_display()} - {self.label}"


class PricingPlan(models.Model):
    section = models.ForeignKey(
        Section, related_name='pricing_plans', on_delete=models.CASCADE,
        blank=True, null=True
    )
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, blank=True)  # "Custom", "$499/mo", etc.
    description = models.TextField(blank=True)
    features = models.JSONField(default=list, blank=True)  # list of strings
    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=500, blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default="Divergent Physics")
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    calendar_link = models.URLField(blank=True)
    copyright_text = models.CharField(max_length=255, blank=True)
    social_links = models.JSONField(blank=True, null=True, default=dict)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return self.site_name


class Lead(models.Model):
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    solver_used = models.CharField(max_length=255, blank=True)
    workflow_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.company_name} - {self.email}"