from django.shortcuts import render
from django.views.generic import View, TemplateView


class SelectgenderView(TemplateView):
    template_name='Dating/selectgender.html'


def TestView(request):
    return render(request, 'index.html')
  
class FirstView(TemplateView):
    template_name='account/first.html'
    
# G1 accounts
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
  
  


# G2  
class StoryPageView(TemplateView):
    template_name = 'story.html'


class ChangePasswordView(TemplateView):
    template_name = 'change_password.html'


# class ProfileView(TemplateView):
#     template_name = 'user_profile.html'


class UpgradeStoryView(TemplateView):
    template_name = 'upgrade_view_story.html'


class EditMyProfile(TemplateView):
    template_name = 'edite_my_profile.html'
    
  

def settings(request):
    return render(request, 'settings.html')

def privacy_settings(request):
    return render(request, 'privacy_settings.html')

def preferences(request):
    return render(request, 'preference.html')

def filter(request):
    return render(request, 'filter.html')

def user_profile(request):
    return render(request, 'user_profile.html')



def  sent(request):
    return render(request, 'sent.html')

def accept(request):
    return render(request, 'accept.html')


def messgage(request):
    return render(request, 'message.html')

def contact(request):
    return render(request, 'contacted.html')

def shortlist(request):
    return render(request, 'shortlist.html')

def shortlist_by(request):
    return render(request, 'shortlist_by.html')


def received(request):
    return render(request, 'received.html')

def reject(request):
    return render(request, 'reject.html')

def viewed_myprofile(request):
    return render(request, 'viewed_myprofile.html')
  
#   G3
class Error403View(TemplateView):
    template_name='error_page/error403.html'
    

class Error404View(TemplateView):
    template_name='error_page/error404.html'


class HomeView(TemplateView):
    template_name = 'home.html'

class DiscoverView(TemplateView):
    template_name = 'discover.html'

class QualificationView(TemplateView):
    template_name = 'qualification.html'

class LocationView(TemplateView):
    template_name = 'location.html'

class DesignationView(TemplateView):
    template_name = 'designation.html'

class MatchView(TemplateView):
    template_name = 'matches.html'

class ProfileviewView(TemplateView):
    template_name = 'profileviews.html'

class UpgradeView(TemplateView):
    template_name = 'upgradepage.html'

class SpinView(TemplateView):
    template_name = 'spin.html'


