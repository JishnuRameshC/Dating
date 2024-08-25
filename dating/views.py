from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def TestView(request):
    return render(request, 'index.html')
class FirstView(TemplateView):
    template_name='account/first.html'

class SignupView(TemplateView):
    template_name='account/signup.html'


class LoginView(TemplateView):
    template_name='account/login.html'
    
class PersonalDetailsView(TemplateView):
    template_name='account/personal_details.html'

class JobStatusView(TemplateView):
    template_name='account/job_status.html'
    
class JobDetailsView(TemplateView):
    template_name='account/job_details.html'


class ProfessionView(TemplateView):
    template_name='account/profession.html'


class Rel_GoalView(TemplateView):
    template_name='account/relationship_goal.html'


class InterestView(TemplateView):
    template_name='account/interested.html'
    

# Group 
class CreateGroupView(TemplateView):
    template_name='groups/create_group.html'


class GroupListView(TemplateView):
    template_name = 'groups/groups.html'


# SubscriptionPlan
class SubscriptionPlanView(TemplateView):
    template_name = 'payment/subscription_plans.html'


class PaymentMethodsView(TemplateView):
    template_name = 'payment/payment_methods.html'


class AddPaymentMethodsView(TemplateView):
    template_name = 'payment/add_payment.html'