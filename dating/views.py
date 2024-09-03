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
    template_name = 'User_profile/story.html'


class ChangePasswordView(TemplateView):
    template_name = 'User_profile/change_password.html'


# class ProfileView(TemplateView):
#     template_name = 'user_profile.html'


class UpgradeStoryView(TemplateView):
    template_name = 'User_profile/upgrade_view_story.html'


class EditMyProfile(TemplateView):
    template_name = 'User_profile/edite_my_profile.html'
    
  

def settings(request):
    return render(request, 'User_profile/settings.html')

def privacy_settings(request):
    return render(request, 'User_profile/privacy_settings.html')

def preferences(request):
    return render(request, 'User_profile/preference.html')

def filter(request):
    return render(request, 'User_profile/filter.html')

def user_profile(request):
    return render(request, 'User_profile/user_profile.html')



def  sent(request):
    return render(request, 'contents/sent.html')

def accept(request):
    return render(request, 'contents/accept.html')


def messgage(request):
    return render(request, 'contents/message.html')

def contact(request):
    return render(request, 'contents/contact.html')

def shortlist(request):
    return render(request, 'contents/shortlist.html')

def shortlist_by(request):
    return render(request, 'contents/shortlist_by.html')


def received(request):
    return render(request, 'contents/received.html')

def reject(request):
    return render(request, 'contents/reject.html')

def viewed_myprofile(request):
    return render(request, 'contents/viewed_myprofile.html')
  
#   G3
class Error403View(TemplateView):
    template_name='error_page/error403.html'
    

class Error404View(TemplateView):
    template_name='error_page/error404.html'


class HomeView(TemplateView):
    template_name = 'Dating/home.html'

class DiscoverView(TemplateView):
    template_name = 'Dating/discover.html'

class QualificationView(TemplateView):
    template_name = 'Dating/qualification.html'

class LocationView(TemplateView):
    template_name = 'Dating/location.html'

class DesignationView(TemplateView):
    template_name = 'Dating/designation.html'

class MatchView(TemplateView):
    template_name = 'Dating/matches.html'

class ProfileviewView(TemplateView):
    template_name = 'Dating/profileviews.html'

class UpgradeView(TemplateView):
    template_name = 'Dating/upgradepage.html'

class SpinView(TemplateView):
    template_name = 'Dating/spin.html'


