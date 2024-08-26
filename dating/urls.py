from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
#     G1 accounts
     path('', views.TestView, name='test'),
    #accounts
    path('first',views.FirstView.as_view(),name='first'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup',views.SignupView.as_view(),name='signup'),
    path('personal_details',views.PersonalDetailsView.as_view(),name='personal_details'),
    path('job_status',views.JobStatusView.as_view(),name="job_status"),
    path('job_details',views.JobDetailsView.as_view(),name="job_Details"),
    path('profession',views.ProfessionView.as_view(),name='profession'),
    
    
    #groups
    path('create_group',views.CreateGroupView.as_view(),name='create_group'),
    path('groupslist',views.GroupListView.as_view(),name='group_list'),
    
    #payment
    path('subscriptionplan/', views.SubscriptionPlanView.as_view(), name='subscription_plan'),
    path('paymentmethods/', views.PaymentMethodsView.as_view(), name='payment_methods'),
    path('addpaymentmethods/', views.AddPaymentMethodsView.as_view(), name='add_payment_methods'),
  
  
#   G2  userprofile_flow
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

    path('message', views.messgage, name='message'),
    path('contact', views.contact, name='contact'),
    path('shortlist', views.shortlist, name='shortlist'),
    path('shortlist_by', views.shortlist_by, name='shortlist_by'),
    path('received', views.received, name='received'),
    path('reject', views.reject, name='reject'),
    path('viewed_myprofile', views.viewed_myprofile, name='viewed_myprofile'),
    path('sent', views.sent, name='sent'),
    path('accept', views.accept, name='accept'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)