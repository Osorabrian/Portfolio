from django.shortcuts import render
from .models import Project
from .forms import SearchForm

# Create your views here.
def projects_list(request):
    
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search']
            projects = Project.objects.filter(title__icontains=query)
            
    else:
        form = SearchForm()
        projects = Project.objects.all().order_by('published')
        
    return render(
        request,
        'projects/projects.html',
        {'projects':projects, 'form':form}
    )
