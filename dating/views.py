from datetime import date
from django.views import View
from django.views.generic import FormView, ListView, TemplateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django import forms 
from django.utils import timezone 
from accounts.models import CustomUser, PersonalDetails, JobProfile, Address
from dating.forms import FilterPreferencesForm, UserFilterForm



class SelectgenderView(TemplateView):
    template_name='Dating/selectgender.html'


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

def privacy(request):
    return render(request, 'User_profile/privacy_settings.html')

class PartnerFilterPreferencesView(LoginRequiredMixin, FormView):
    template_name = 'User_profile/preference.html'
    form_class = FilterPreferencesForm
    success_url = reverse_lazy('dating:match')  # Redirect to results page after filtering

    def form_valid(self, form):
        # Store filter data in session
        self.request.session['filter_data'] = form.cleaned_data
        return redirect(self.success_url)
    
class FilterResultsView(LoginRequiredMixin, ListView):
    template_name = 'dating/matches.html'
    context_object_name = 'users'

    def get_queryset(self):
        # Get filter data from session
        filter_data = self.request.session.get('filter_data', {})
        age_min = filter_data.get('age_min', 18)
        age_max = filter_data.get('age_max', 35)
        gender = filter_data.get('gender', 'any')
        location = filter_data.get('location', None)
        hobbies = filter_data.get('hobbies', None)
        occupation = filter_data.get('occupation', 'any')
        religion = filter_data.get('religion', 'any')

        # Start with all users
        queryset = CustomUser.objects.all()

        # Get current year
        today = date.today()

        # Apply age filter: calculate year range from dob based on age_min and age_max
        if age_min and age_max:
            birth_year_min = today.year - int(age_max)
            birth_year_max = today.year - int(age_min)
            queryset = queryset.filter(personaldetails__dob__year__range=(birth_year_min, birth_year_max))

        # Apply other filters
        if gender != 'any':
            queryset = queryset.filter(personaldetails__gender=gender)

        if location:
            queryset = queryset.filter(address__city__icontains=location)

        if hobbies:
            queryset = queryset.filter(personaldetails__hobbies__icontains=hobbies)

        if occupation != 'any':
            queryset = queryset.filter(jobprofile__job_status=occupation)

        if religion != 'any':
            queryset = queryset.filter(personaldetails__religion=religion)

        return queryset
    
# def filter(request):
#     return render(request, 'User_profile/filter.html')

# class DiscoverView(TemplateView):
#     template_name = 'dating/discover.html'


class FilterPreferencesView(LoginRequiredMixin, FormView):
    template_name = 'User_profile/filter.html'
    form_class = UserFilterForm  # Use the new form
    success_url = reverse_lazy('dating:discover')  # Redirect to discover page after filtering

    def form_valid(self, form):
        # Store filter data in session
        self.request.session['filter_data'] = form.cleaned_data
        return redirect(self.success_url)

class DiscoverView(LoginRequiredMixin, ListView):
    template_name = 'dating/discover.html'
    context_object_name = 'users'

    def get_queryset(self):
        # Get filter data from session
        filter_data = self.request.session.get('filter_data', {})
        sort_by = filter_data.get('sort_by', 'newest')
        gender = filter_data.get('gender', 'any')
        location = filter_data.get('location', None)
        hobbies = filter_data.get('hobbies', None)
        languages_spoken = filter_data.get('languages_spoken', None)
        relationship_goals = filter_data.get('relationship_goals', 'any')

        # Start with all users
        queryset = CustomUser.objects.all()

        # Apply filters

        # Gender Filter
        if gender != 'any':
            queryset = queryset.filter(personaldetails__gender=gender)

        # Location Filter (Multiple locations)
        if location:
            location_list = [loc.strip() for loc in location.split(',')]  # Split by comma, strip spaces
            queryset = queryset.filter(address__city__in=location_list)

        # Hobbies Filter
        if hobbies:
            queryset = queryset.filter(personaldetails__hobbies__icontains=hobbies)

        # Languages Spoken Filter
        if languages_spoken:
            queryset = queryset.filter(personaldetails__languages_spoken__icontains=languages_spoken)

        # Relationship Goals Filter
        if relationship_goals != 'any':
            queryset = queryset.filter(personaldetails__relationship_goals=relationship_goals)

        # Apply sorting logic
        if sort_by == 'newest':
            queryset = queryset.order_by('-date_joined')  # Assuming CustomUser has a date_joined field
        elif sort_by == 'last_active':
            queryset = queryset.order_by('-last_login')  # Assuming CustomUser has a last_login field
        elif sort_by == 'distance':
            # Distance-based sorting logic (if implemented)
            pass
        elif sort_by == 'popularity':
            # Popularity-based sorting logic (if implemented)
            pass
        elif sort_by == 'age':
            queryset = queryset.order_by('personaldetails__dob')  # Sort by age (youngest first)

        return queryset

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


class Error403View(TemplateView):
    template_name='error_page/error403.html'
    

class Error404View(TemplateView):
    template_name='error_page/error404.html'


class HomeView(TemplateView):
    template_name = 'Dating/home.html'

class QualificationView(TemplateView):
    template_name = 'Dating/qualification.html'

class LocationView(TemplateView):
    template_name = 'Dating/location.html'

class DesignationView(TemplateView):
    template_name = 'Dating/designation.html'


class ProfileviewView(TemplateView):
    template_name = 'Dating/profileviews.html'

class UpgradeView(TemplateView):
    template_name = 'User_profile/upgrade_to_view_profile.html'

class SpinView(TemplateView):
    template_name = 'Dating/spin.html'