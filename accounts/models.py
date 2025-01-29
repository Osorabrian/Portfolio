from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

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

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE
    )
    photo = models.ImageField(upload_to='profiles/%Y/%m/%d/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} profile has been created"
    
    class Meta:
        ordering = ['user']
        indexes = [
            models.Index(fields=['user'])
            ]