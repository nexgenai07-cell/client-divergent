# blog/models.py
from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    external_link = models.URLField(blank=True)
    
    # New fields from reference image
    author = models.CharField(max_length=200, blank=True, null=True)
    read_time = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., '5 min read'")
    
    published_date = models.DateField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date', 'order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title