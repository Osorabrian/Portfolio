from django.db import models

# Create your models here.
class Education(models.Model):
    school=models.CharField(max_length=250)
    course=models.CharField(max_length=250)
    start_year=models.DateField()
    end_year=models.DateField()
    description=models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.school} added."
    
    class Meta:
        ordering = ['-school']
        indexes = [
            models.Index(fields=['-school']),
        ]

