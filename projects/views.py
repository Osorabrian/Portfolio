from django.shortcuts import render
from .models import Project
from .forms import SearchForm
from django.core.paginator import Paginator

# Create your views here.
def projects_list(request):
    
    query = None
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search']
    else:
        form = SearchForm()

    if query:
        projects = Project.objects.filter(title__icontains=query).order_by('published') 
    else:
        projects = Project.objects.all().order_by('published')
        
    paginator = Paginator(projects, 5)
    page_number = request.GET.get('page', 1)
    projects = paginator.page(page_number)
        
    return render(
        request,
        'projects/projects.html',
        {'projects':projects, 'form':form}
    )
