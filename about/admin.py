from django.contrib import admin
from .models import Education, Experience

# Register your models here.
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['school','course','start_date','end_date']
    list_filter = ['school']
    date_hierachy = 'start_date'
    search_fields = ['school','course']
    show_facets = admin.ShowFacets.ALWAYS
    
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company','position','start_date','end_date']
    list_filter = ['company']
    date_hierachy = ['start_date']
    search_fields = ['school','position','achievement']
    show_facets = admin.ShowFacets.ALWAYS    