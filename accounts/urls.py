from django.urls  import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.home, name="home"),
    path('message', views.message, name="message"),
    path('create_account/', views.user_registration, name="user_registration"),
    path('edit_profile', views.profile, name="profile")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )