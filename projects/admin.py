from django.contrib import admin
from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'url', 'status']
    list_filter = ['title', 'status']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug':('title',)}
    date_hierachy = 'published'
    ordering = ['title']
    show_facets = admin.ShowFacets.ALWAYS
