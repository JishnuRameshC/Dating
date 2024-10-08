from django.urls import path
from . import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    
    path('logout/',views.signout, name='logout'),
    path('first',views.FirstView.as_view(),name='first'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup',views.SignupView.as_view(),name='signup'),
    path('personal_details',views.PersonalDetailsCreateView.as_view(),name='personal_details'),
    
    path('job_status',views.JobStatusView.as_view(),name="job_status"),
    path('job-details/<int:user_id>/', EmployerDetailsView.as_view(), name='job_Details'),

    path('profession/<int:user_id>/',views.EmployeeDetailsView.as_view(),name='profession'),
    path('relationship_goal/<int:user_id>/', RelationshipGoalsView.as_view(), name='relationship_goal'),
    path('interest',views.InterestView.as_view(),name='interest'),
                  
              ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)