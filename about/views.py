from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(
        request,
        'about/about.html'
    )
    
def education_view(request):
    return render(
        request,
        'about/includes/education.html'
    )
    
def experience_view(request):
    return render(
        request,
        'about/includes/experience.html'
    )