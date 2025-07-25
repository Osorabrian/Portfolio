from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    thumbnail = models.ImageField(upload_to='blogs/%Y/%m/%d/', blank=True, null=True)
    content = models.TextField()
    tags = TaggableManager()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    published = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'blogs:post_detail',
            args=[
                self.published.year,
                self.published.month,
                self.published.day,
                self.slug
            ]
        )
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-published']
        indexes = [models.Index(fields=['-published'])]

    