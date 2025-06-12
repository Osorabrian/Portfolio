from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_display = ['title', 'status', 'published' ]
    date_hierarchy = 'published'
    list_filter = ['status', 'published']
    ordering = ['-published']
    show_facets = admin.ShowFacets.ALWAYS