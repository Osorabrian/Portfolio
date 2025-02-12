from django.urls import path
from . import views

app_name = "about"

urlpatterns = [
    path('', views.experience_view, name="experoence"),
    path('', views.education_view, name="education")
]