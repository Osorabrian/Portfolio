from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message=models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} has written a message"
    
    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published'])
            ]