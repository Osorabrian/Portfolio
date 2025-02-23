from django.urls  import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('password_reset/', views.CustomPasswordResetFormView.as_view(), name="password_reset"),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name="password_change"),
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