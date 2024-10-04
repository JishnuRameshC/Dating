from django.shortcuts import render
from django.views.generic import View,TemplateView




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


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Story, Comment, FriendRequest, Shortlist, ProfileView
from accounts.models import CustomUser

# View for the Accept page
def accept_view(request):
    return render(request, 'your_template_name.html')  # Replace with actual template name

# Story List View
class StoryListView(ListView):
    model = Story
    template_name = 'story_list.html'
    context_object_name = 'stories'

# Story Detail View (with comments)
class StoryDetailView(DetailView):
    model = Story
    template_name = 'story_detail.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(story=self.get_object())
        return context

# Story Create View
class StoryCreateView(CreateView):
    model = Story
    fields = ['caption']
    template_name = 'story_form.html'
    success_url = reverse_lazy('story_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Add a comment to a story
def add_comment(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(story=story, user=request.user, text=text)
            return redirect('story_detail', pk=story.id)
    return redirect('story_detail', pk=story.id)

# Send Friend Request
def send_friend_request(request, user_id):
    receiver = get_object_or_404(CustomUser, id=user_id)
    FriendRequest.objects.create(sender=request.user, receiver=receiver, status='sent')
    return redirect('user_profile', pk=user_id)

# Accept Friend Request
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if request.user == friend_request.receiver:
        friend_request.status = 'accepted'
        friend_request.save()
    return redirect('friend_requests')

# Shortlist a User
def shortlist_user(request, user_id):
    shortlisted_user = get_object_or_404(CustomUser, id=user_id)
    Shortlist.objects.create(user=request.user, shortlisted_user=shortlisted_user)
    return redirect('shortlist')

# View Profile View List
class ProfileViewListView(ListView):
    model = ProfileView
    template_name = 'profile_view_list.html'
    context_object_name = 'profile_views'

    def get_queryset(self):
        return ProfileView.objects.filter(viewed_user=self.request.user)

# Create a new Profile View
def create_profile_view(request, user_id):
    viewed_user = get_object_or_404(CustomUser, id=user_id)
    ProfileView.objects.create(viewer=request.user, viewed_user=viewed_user)
    return redirect('profile', pk=user_id)
