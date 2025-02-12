from django.shortcuts import render
from .models import Experience, Education

# Create your views here.
def education_view(request):
    education = Education.objects.all()
    return render(
        request,
        'about/about.html',
        {'education':education}
    )
    
def experience_view(request):
    experience = Experience.objects.all()
    return render(
        request,
        'about/about.html',
        {'experience':experience}
    )