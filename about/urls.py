from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "about"

urlpatterns = [
    path('', views.experience_view, name="experoence"),
    path('', views.education_view, name="education")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root= settings.MEDIA_ROOT
    )