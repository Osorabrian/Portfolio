from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    
    class Status(models.TextChoices):
        CP = 'CP', 'Completed'
        IP = 'IP', 'In Progress'
    
    title = models.CharField(max_length=80)
    slug = models.CharField(max_length=80)
    description = models.TextField()
    url = models.URLField()
    github = models.URLField()
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.IP
    )
    published  = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} has been created"
    
    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published', 'title'])
        ]
    