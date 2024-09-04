from django.shortcuts import render
from django.views.generic import View, TemplateView,ListView
from accounts.models import CustomUser, Address,PersonalDetails,JobProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404



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



class HomeView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = 'Dating/home.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get current user's city, qualification, and designation if authenticated
        if self.request.user.is_authenticated:
            try:
                address = self.request.user.address_set.first()
                user_city = address.city if address else None
                user_qualification = self.request.user.personaldetails.qualifications
                user_designation = self.request.user.jobprofile.designation  # Accessing designation from JobProfile
            except (PersonalDetails.DoesNotExist, JobProfile.DoesNotExist):
                user_city = None
                user_qualification = None
                user_designation = None

            # Retrieve all users excluding superusers
            users = CustomUser.objects.exclude(is_superuser=True)

            # Filter users based on selected filters
            filter_city = self.request.GET.get('filter_city', None)
            filter_qualification = self.request.GET.get('filter_qualification', None)
            filter_designation = self.request.GET.get('filter_designation', None)

            if filter_city and filter_city != user_city:
                users = users.filter(address__city=filter_city)
            if filter_qualification and filter_qualification != user_qualification:
                users = users.filter(personaldetails__qualifications=filter_qualification)
            if filter_designation and filter_designation != user_designation:
                users = users.filter(jobprofile__designation=filter_designation)

            context['users'] = users
            context['user_city'] = user_city
            context['user_qualification'] = user_qualification
            context['user_designation'] = user_designation

        return context
    

# class HomeView(LoginRequiredMixin, TemplateView):
#     model = CustomUser
#     template_name = 'Dating/home.html'
#     context_object_name = 'users'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Get current user's city, qualification, designation, and interests if authenticated
#         if self.request.user.is_authenticated:
#             try:
#                 address = self.request.user.address_set.first()
#                 user_city = address.city if address else None
#                 user_qualification = self.request.user.personaldetails.qualifications
#                 user_designation = self.request.user.jobprofile.designation  # Accessing designation from JobProfile
#                 user_interests = self.request.user.personaldetails.interests
#             except (PersonalDetails.DoesNotExist, JobProfile.DoesNotExist):
#                 user_city = None
#                 user_qualification = None
#                 user_designation = None
#                 user_interests = None

#             # Retrieve all users excluding superusers
#             users = CustomUser.objects.exclude(is_superuser=True)

#             # Filter users based on selected filters
#             filter_city = self.request.GET.get('filter_city', None)
#             filter_qualification = self.request.GET.get('filter_qualification', None)
#             filter_designation = self.request.GET.get('filter_designation', None)

#             if filter_city and filter_city != user_city:
#                 users = users.filter(address__city=filter_city)
#             if filter_qualification and filter_qualification != user_qualification:
#                 users = users.filter(personaldetails__qualifications=filter_qualification)
#             if filter_designation and filter_designation != user_designation:
#                 users = users.filter(jobprofile__designation=filter_designation)

#             # Exclude users whose gender is not of interest to the logged-in user
#             if user_interests:
#                 if user_interests == 'M':
#                     users = users.filter(personaldetails__gender='M')
#                 elif user_interests == 'F':
#                     users = users.filter(personaldetails__gender='F')
#                 elif user_interests == 'B':
#                     # If user is interested in both genders, no additional filter is needed
#                     pass

#             context['users'] = users
#             context['user_city'] = user_city
#             context['user_qualification'] = user_qualification
#             context['user_designation'] = user_designation

#         return context



class DiscoverView(TemplateView):
    template_name = 'Dating/discover.html'

class QualificationView(TemplateView):
    template_name = 'Dating/qualification.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_in_user = self.request.user

        # Get the logged-in user's qualification
        logged_in_user_details = logged_in_user.personaldetails

        # Filter users with the same qualification as the logged-in user
        similar_profiles = CustomUser.objects.filter(personaldetails__qualifications=logged_in_user_details.qualifications).exclude(id=logged_in_user.id)

        context['similar_profiles'] = similar_profiles
        return context
    

class LocationView(TemplateView):
    template_name = 'Dating/location.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Get the city of the logged-in user from their address
        user_city = Address.objects.filter(user=user).values_list('city', flat=True).first()

        if user_city:
            # Filter profiles based on the same city
            profiles_in_city = CustomUser.objects.filter(address__city=user_city).exclude(id=user.id)

            # Prepare the list of matches with scores
            matches = []
            try:
                user_personal_details = user.personaldetails
            except PersonalDetails.DoesNotExist:
                user_personal_details = None

            for profile in profiles_in_city:
                try:
                    profile_personal_details = profile.personaldetails
                    if user_personal_details:
                        # Calculate match score
                        match_score = user_personal_details.calculate_match_score(profile_personal_details)
                        matches.append((profile, match_score))
                except PersonalDetails.DoesNotExist:
                    continue

            # Sort matches by score in descending order
            matches.sort(key=lambda x: x[1], reverse=True)
            
            context['profiles'] = matches
        else:
            # If the user doesn't have a city in their address, return an empty queryset
            context['profiles'] = []

        return context


class DesignationView(TemplateView):
    template_name = 'Dating/designation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = get_object_or_404(JobProfile, user=self.request.user)
        
        # Filter out the current user by excluding the logged-in user's ID
        same_designation_profiles = JobProfile.objects.filter(designation=user_profile.designation).exclude(user=self.request.user)
        
        # Prepare the list of matches with scores
        matches = []
        for profile in same_designation_profiles:
            # Get PersonalDetails for each profile
            try:
                user_personal_details = profile.user.personaldetails
                current_user_personal_details = self.request.user.personaldetails
                # Calculate match score
                match_score = current_user_personal_details.calculate_match_score(user_personal_details)
                matches.append((profile.user, match_score))
            except PersonalDetails.DoesNotExist:
                continue

        # Sort matches by score in descending order
        matches.sort(key=lambda x: x[1], reverse=True)
        
        context['profiles'] = same_designation_profiles
        context['matches'] = matches
        return context

class MatchView(LoginRequiredMixin, ListView):
    template_name = 'contents/matches.html'
    context_object_name = 'matches'

    def get_queryset(self):
        try:
            user_details = self.request.user.personaldetails
        except PersonalDetails.DoesNotExist:
            # Handle the case where PersonalDetails for the logged-in user doesn't exist
            return []

        matches = self.find_matching_profiles(user_details)
        return matches

    def find_matching_profiles(self, user_details):
        matches = []
        
        for other_user_details in PersonalDetails.objects.exclude(user=user_details.user):
            match_score = user_details.calculate_match_score(other_user_details)
            if match_score > 50:  # Set a threshold for matching
                matches.append((other_user_details.user, match_score))
        
        # Sort by highest match score
        matches.sort(key=lambda x: x[1], reverse=True)
        
        return matches

class ProfileviewView(TemplateView):
    template_name = 'Dating/profileviews.html'

class UpgradeView(TemplateView):
    template_name = 'Dating/upgradepage.html'

class SpinView(TemplateView):
    template_name = 'Dating/spin.html'


