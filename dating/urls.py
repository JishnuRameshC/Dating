from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
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
    
              ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)