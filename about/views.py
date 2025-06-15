from django.shortcuts import render
from .models import Education, Experience

# Create your views here.
def about_view(request):
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    return render(
        request,
        'about/about.html',
        {
            'educations': educations,
            'experiences': experiences
        }
    )