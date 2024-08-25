from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        path('settings/', views.settings, name='settings'),
        path('privacy_settings', views.privacy_settings, name='privacy_settings'),
        path('preferences', views.preferences, name='preferences'),
        path('filter', views.filter, name='filter'),
        path('user', views.user_profile, name='user_profile'),
              ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)