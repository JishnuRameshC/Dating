from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView,ListView
from accounts.models import CustomUser, Address,PersonalDetails,JobProfile
from .models import Interestin, ProfileView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404



def TestView(request):
    return render(request, 'index.html')
  

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


class UserProfileView(TemplateView):
    template_name = 'User_profile/user_profile.html'


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
    return render(request, 'contents/contacted.html')

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

class SelectgenderView(LoginRequiredMixin,TemplateView):
    template_name = 'Dating/selectgender.html'
    success_url = reverse_lazy('dating:home')

    def post(self, request, *args, **kwargs):
        interestin_value = request.POST.get('interested_in')
        if interestin_value:
            Interestin.objects.update_or_create(
                user=self.request.user,
                defaults={'interestin': interestin_value}
            )
        return redirect(self.success_url)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

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
    template_name = 'contents/matches.html'
   


class UpgradeView(TemplateView):
    template_name = 'Dating/upgradepage.html'

class SpinView(TemplateView):
    template_name = 'Dating/spin.html'


class ProfileviewView(LoginRequiredMixin,ListView):
    model = ProfileView
    template_name = 'Dating/profileviews.html'  
    context_object_name = 'profile_views'

    def get_queryset(self):
        
        return ProfileView.objects.filter(viewer=self.request.user).order_by('-viewed_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['profile_view_count'] = self.get_queryset().count()

        return context