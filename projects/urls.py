from django.urls import path
from . import views

namespace = "projects"
urlpatterns = [
    path("", views.projects_list, name="projects"),
    path("<str:query>", views.projects_list, name="projects_search")
]