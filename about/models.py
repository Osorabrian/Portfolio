from django.db import models

# Create your models here.
class Education(models.Model):
    school = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.course} taken at {self.school} added."
    
    class Meta:
        ordering = ['-start_date']
        indexes = [
            models.Index(fields=['-start_date']),
        ]
        
class Experience(models.Model):
    company = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.position} at {self.company} added."
    
    class Meta:
        ordering = ['-start_date']
        indexes = [
            models.Index(fields=['-start_date']),
        ]