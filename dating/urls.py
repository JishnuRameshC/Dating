from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Dating'

   


urlpatterns = [
#     G1 accounts
     path('', views.TestView, name='test'),
    #accounts
    
    
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
    path('story/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),

    path('profile/<str:username>/', views.UserProfileView.as_view(), name='profile'),
    # Match Requests
    path('send_request/', SendRequestView.as_view(), name='send_request'),
    path('received_requests/', ReceiveRequestView.as_view(), name='received_requests'),
    path('accept_request/', AcceptRequestView.as_view(), name='accept_request'),
    path('reject_request/', RejectRequestView.as_view(), name='reject_request'),
    path('shortlist/', ShortlistView.as_view(), name='shortlist_user'),

# 
    
    # Contacted
    path('contact/<str:username>/', ContactUserView.as_view(), name='contact_user'),
    
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),    path('upgrade/',views.UpgradeStoryView.as_view(),name="upgrade"),
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
    
#     G3
    path("selectgender/", SelectgenderView.as_view(), name="selectgender"),
    path("error403/", Error403View.as_view(), name="error403"),
    path("error404/", Error404View.as_view(), name="error404"),
    path('home/', HomeView.as_view(), name='home'),
    path('discover/', DiscoverView.as_view(), name='discover'),   
    path('qualification/', QualificationView.as_view(), name='qualification'),    
    path('location/', LocationView.as_view(), name='location'),   
    path('designation/', DesignationView.as_view(), name='designation'),  
    path('match/', MatchView.as_view(), name='match'),  
    path('profile_view/', ProfileviewView.as_view(), name='profile_view'),  
    path('upgrade/', UpgradeView.as_view(), name='upgrade'),   
    path('spin/', SpinView.as_view(), name='spin'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)