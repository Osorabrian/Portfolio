from django.shortcuts import render
from .models import Project

# Create your views here.
def projects_list(request):
    projects = Project.objects.all().order_by('published')
    return render(
        request,
        'projects/projects.html',
        {'projects':projects}
    )
