from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import FilterPreferencesView, FilterResultsView
app_name = 'dating'

   


urlpatterns = [
#     G1 accounts
    #  path('', views.TestView, name='test'),
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
    path('privacy/', views.privacy, name='privacy'),



    path('preferences/', PartnerFilterPreferencesView.as_view(), name='preferences'),
    path('match/', views.FilterResultsView.as_view(), name='match'),
    path('filter/', FilterPreferencesView.as_view(), name='filter_preferences'),
    path('discover/', DiscoverView.as_view(), name='discover'),   



    # path('filter', views.filter, name='filter'),
    path('user/', views.user_profile, name='user'),

    path('test', views.TestView, name='test'),
    path('story/', views.StoryPageView.as_view(), name='story'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
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
    
#     G3
    path("selectgender/", SelectgenderView.as_view(), name="selectgender"),
    path("error403/", Error403View.as_view(), name="error403"),
    path("error404/", Error404View.as_view(), name="error404"),
    path('home/', HomeView.as_view(), name='home'),


   

    path('qualification/', QualificationView.as_view(), name='qualification'),    
    path('location/', LocationView.as_view(), name='location'),   
    path('designation/', DesignationView.as_view(), name='designation'),  
    # path('match/', MatchesView.as_view(), name='match'),  
    path('profile_view/', ProfileviewView.as_view(), name='profile_view'),  
    path('upgrade_profile/', UpgradeView.as_view(), name='upgrade'),   
    path('spin/', SpinView.as_view(), name='spin'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)