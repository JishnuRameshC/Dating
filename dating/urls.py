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

    path('test', views.TestView, name='test'),
    path('story/', views.StoryPageView.as_view(), name='story'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('upgrade/',views.UpgradeStoryView.as_view(),name="upgrade"),
    path('edite_profile/',views.EditMyProfile.as_view(),name="edite_profile"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)