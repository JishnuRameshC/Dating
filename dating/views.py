from django.shortcuts import render
from django.views.generic import View, TemplateView,ListView
from accounts.models import CustomUser, Address,PersonalDetails,JobProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import random
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from datetime import timedelta
from django.utils import timezone


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

        if self.request.user.is_authenticated:
            try:
                # Get current user's personal details
                user_details = self.request.user.personaldetails
                user_city = self.request.user.address_set.first().city if self.request.user.address_set.exists() else None
                user_qualification = user_details.qualifications
                user_designation = self.request.user.jobprofile.designation
                user_interest = user_details.interests  # Logged-in user's interest (M/F/B)
                user_short_reel = user_details.short_reel
            except (PersonalDetails.DoesNotExist, JobProfile.DoesNotExist):
                user_city = None
                user_qualification = None
                user_designation = None
                user_interest = None
                user_short_reel = None

            # Retrieve all users excluding superusers
            users = CustomUser.objects.exclude(is_superuser=True).exclude(pk=self.request.user.pk)  # Exclude the logged-in user

            # Filter users based on the logged-in user's interest
            if user_interest == 'M':
                users = users.filter(personaldetails__gender='M')
            elif user_interest == 'F':
                users = users.filter(personaldetails__gender='F')
            elif user_interest == 'B':
                # If interested in both, don't filter by gender
                pass

            # Apply additional filters (if provided)
            filter_city = self.request.GET.get('filter_city', None)
            filter_qualification = self.request.GET.get('filter_qualification', None)
            filter_designation = self.request.GET.get('filter_designation', None)

            if filter_city and filter_city != user_city:
                users = users.filter(address__city=filter_city)
            if filter_qualification and filter_qualification != user_qualification:
                users = users.filter(personaldetails__qualifications=filter_qualification)
            if filter_designation and filter_designation != user_designation:
                users = users.filter(jobprofile__designation=filter_designation)

            # Add online status for each user
            for user in users:
                user.is_online = user.last_activity and timezone.now() - user.last_activity <= timedelta(minutes=5)

            # Pass relevant data to the context
            context['users'] = users
            context['user_city'] = user_city
            context['user_qualification'] = user_qualification
            context['user_designation'] = user_designation
            context['user_short_reel'] = user_short_reel

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

        # Initialize geolocator
        geolocator = Nominatim(user_agent="your_app_name")

        # Get the logged-in user's qualifications, address, and interests
        try:
            logged_in_user_details = logged_in_user.personaldetails
            logged_in_user_address = logged_in_user.address_set.filter(is_default=True).first()
            user_interest = logged_in_user_details.interests

            # Get coordinates of the logged-in user's address
            logged_in_user_coords = self.get_coordinates(logged_in_user_address, geolocator)
        except PersonalDetails.DoesNotExist:
            # Handle case where the logged-in user doesn't have personal details
            context['similar_profiles'] = []
            context['matches'] = []
            return context

        # Filter profiles based on the logged-in user's interests
        if user_interest == 'M':
            similar_profiles = CustomUser.objects.filter(
                personaldetails__qualifications=logged_in_user_details.qualifications,
                personaldetails__gender='M'
            ).exclude(id=logged_in_user.id)
        elif user_interest == 'F':
            similar_profiles = CustomUser.objects.filter(
                personaldetails__qualifications=logged_in_user_details.qualifications,
                personaldetails__gender='F'
            ).exclude(id=logged_in_user.id)
        else:  # 'B' for both
            similar_profiles = CustomUser.objects.filter(
                personaldetails__qualifications=logged_in_user_details.qualifications
            ).exclude(id=logged_in_user.id)

        # Prepare the list of matches with scores, distances, and online status
        matches = []
        for profile in similar_profiles:
            try:
                user_personal_details = profile.personaldetails
                profile_address = profile.address_set.filter(is_default=True).first()

                # Get coordinates of each profile's address
                profile_coords = self.get_coordinates(profile_address, geolocator)

                # Calculate match score
                match_score = logged_in_user_details.calculate_match_score(user_personal_details)

                # Calculate distance
                if logged_in_user_coords and profile_coords:
                    distance = geodesic(logged_in_user_coords, profile_coords).km
                else:
                    distance = None

                # Determine if the user is online
                is_online = profile.is_online()

                matches.append((profile, match_score, distance, is_online))
            except PersonalDetails.DoesNotExist:
                continue

        # Sort matches by score in descending order
        matches.sort(key=lambda x: x[1], reverse=True)

        context['similar_profiles'] = similar_profiles
        context['matches'] = matches
        return context

    def get_coordinates(self, address, geolocator):
        if address:
            try:
                location = geolocator.geocode(f"{address.city}, {address.state}, {address.country}")
                if location:
                    return (location.latitude, location.longitude)
            except:
                return None
        return None

class LocationView(TemplateView):
    template_name = 'Dating/location.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Initialize geolocator
        geolocator = Nominatim(user_agent="your_app_name")

        # Get the logged-in user's address and city
        user_address = Address.objects.filter(user=user, is_default=True).first()
        if user_address:
            user_city = user_address.city
            user_coords = self.get_coordinates(user_address, geolocator)
        else:
            user_city = None
            user_coords = None

        if user_city:
            try:
                # Get logged-in user's personal details and interest
                user_personal_details = user.personaldetails
                user_interest = user_personal_details.interests  # 'M', 'F', or 'B'
            except PersonalDetails.DoesNotExist:
                user_personal_details = None
                user_interest = None

            # Filter profiles based on the same city and logged-in user's interest
            if user_interest == 'M':
                profiles_in_city = CustomUser.objects.filter(
                    address__city=user_city, personaldetails__gender='M'
                ).exclude(id=user.id)
            elif user_interest == 'F':
                profiles_in_city = CustomUser.objects.filter(
                    address__city=user_city, personaldetails__gender='F'
                ).exclude(id=user.id)
            else:  # 'B' for both
                profiles_in_city = CustomUser.objects.filter(address__city=user_city).exclude(id=user.id)

            # Prepare the list of matches with scores, distances, and online status
            matches = []
            for profile in profiles_in_city:
                try:
                    profile_personal_details = profile.personaldetails
                    profile_address = profile.address_set.filter(is_default=True).first()
                    profile_coords = self.get_coordinates(profile_address, geolocator)

                    # Calculate match score
                    if user_personal_details:
                        match_score = user_personal_details.calculate_match_score(profile_personal_details)
                    else:
                        match_score = None

                    # Calculate distance
                    if user_coords and profile_coords:
                        distance = geodesic(user_coords, profile_coords).km
                    else:
                        distance = None

                    # Determine if the user is online
                    is_online = profile.is_online()

                    matches.append((profile, match_score, distance, is_online))
                except PersonalDetails.DoesNotExist:
                    continue

            # Sort matches by score in descending order
            matches.sort(key=lambda x: x[1], reverse=True)
            context['profiles'] = matches
        else:
            context['profiles'] = []

        return context

    def get_coordinates(self, address, geolocator):
        if address and address.address_line_3:
            try:
                location = geolocator.geocode(address.address_line_3)
                if location:
                    return (location.latitude, location.longitude)
            except GeocoderTimedOut:
                print(f"GeocoderTimedOut for address: {address.address_line_3}")
        return None


class DesignationView(TemplateView):
    template_name = 'Dating/designation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = get_object_or_404(JobProfile, user=self.request.user)

        # Initialize geolocator
        geolocator = Nominatim(user_agent="your_app_name")

        # Get the logged-in user's default address and coordinates
        user_address = Address.objects.filter(user=self.request.user, is_default=True).first()
        if user_address:
            user_coords = self.get_coordinates(user_address, geolocator)
        else:
            user_coords = None

        try:
            # Get the logged-in user's personal details and interest
            current_user_personal_details = self.request.user.personaldetails
            user_interest = current_user_personal_details.interests  # 'M', 'F', or 'B'
        except PersonalDetails.DoesNotExist:
            current_user_personal_details = None
            user_interest = None

        # Filter profiles with the same designation and according to logged-in user's interest
        if user_interest == 'M':
            same_designation_profiles = JobProfile.objects.filter(
                designation=user_profile.designation,
                user__personaldetails__gender='M'
            ).exclude(user=self.request.user)
        elif user_interest == 'F':
            same_designation_profiles = JobProfile.objects.filter(
                designation=user_profile.designation,
                user__personaldetails__gender='F'
            ).exclude(user=self.request.user)
        else:  # 'B' for both
            same_designation_profiles = JobProfile.objects.filter(
                designation=user_profile.designation
            ).exclude(user=self.request.user)

        # Prepare the list of matches with scores, distances, and online status
        matches = []
        for profile in same_designation_profiles:
            try:
                user_personal_details = profile.user.personaldetails
                profile_address = Address.objects.filter(user=profile.user, is_default=True).first()
                profile_coords = self.get_coordinates(profile_address, geolocator)

                # Calculate match score
                if current_user_personal_details:
                    match_score = current_user_personal_details.calculate_match_score(user_personal_details)
                else:
                    match_score = None

                # Calculate distance
                if user_coords and profile_coords:
                    distance = geodesic(user_coords, profile_coords).km
                else:
                    distance = None

                # Determine if the user is online
                is_online = profile.user.is_online()

                matches.append((profile.user, match_score, distance, is_online))

            except PersonalDetails.DoesNotExist:
                continue

        # Sort matches by score in descending order
        matches.sort(key=lambda x: x[1], reverse=True)

        context['profiles'] = same_designation_profiles
        context['matches'] = matches
        return context

    def get_coordinates(self, address, geolocator):
        if address and address.address_line_3:
            try:
                location = geolocator.geocode(address.address_line_3)
                if location:
                    return (location.latitude, location.longitude)
            except GeocoderTimedOut:
                print(f"GeocoderTimedOut for address: {address.address_line_3}")
        return None

class MatchView(LoginRequiredMixin, ListView):
    template_name = 'contents/matches.html'
    context_object_name = 'matches'

    def get_queryset(self):
        # Get the logged-in user's personal details
        try:
            user_details = self.request.user.personaldetails
        except PersonalDetails.DoesNotExist:
            # Handle the case where PersonalDetails for the logged-in user doesn't exist
            return []

        # Find matching profiles based on the logged-in user's details
        matches = self.find_matching_profiles(user_details)
        return matches

    def find_matching_profiles(self, user_details):
        # Initialize geolocator
        geolocator = Nominatim(user_agent="your_app_name")

        # Get the logged-in user's default address and coordinates
        user_address = Address.objects.filter(user=user_details.user, is_default=True).first()
        user_coords = self.get_coordinates(user_address, geolocator) if user_address else None

        matches = []

        # Iterate through other users' personal details and calculate matches
        for other_user_details in PersonalDetails.objects.exclude(user=user_details.user):
            # Get the other user's default address and coordinates
            other_user_address = Address.objects.filter(user=other_user_details.user, is_default=True).first()
            other_user_coords = self.get_coordinates(other_user_address, geolocator) if other_user_address else None

            # Calculate match score between logged-in user and other user
            match_score = user_details.calculate_match_score(other_user_details)

            # Calculate distance between logged-in user and other user, if coordinates are available
            if user_coords and other_user_coords:
                distance = geodesic(user_coords, other_user_coords).km
            else:
                distance = None  # If coordinates are unavailable

            # Check if the other user is online
            is_online = other_user_details.user.is_online()

            # Only add matches with a score above 50
            if match_score > 50:
                matches.append((other_user_details.user, match_score, distance, is_online))

        # Sort the matches by match score in descending order
        matches.sort(key=lambda x: x[1], reverse=True)

        return matches

    def get_coordinates(self, address, geolocator):
        if address and address.address_line_3:
            try:
                # Get the latitude and longitude from the geolocator
                location = geolocator.geocode(address.address_line_3)
                if location:
                    return (location.latitude, location.longitude)
            except GeocoderTimedOut:
                print(f"GeocoderTimedOut for address: {address.address_line_3}")
        return None

class ProfileviewView(TemplateView):
    template_name = 'Dating/profileviews.html'

class UpgradeView(TemplateView):
    template_name = 'Dating/upgradepage.html'

class SpinView(TemplateView):
    template_name = 'Dating/spin.html'


class RandomProfileView(View):
    def get(self, request, *args, **kwargs):
        # Get the logged-in user's details
        user_details = PersonalDetails.objects.get(user=request.user)
        
        # Filter profiles based on the logged-in user's interest
        if user_details.interests == 'M':
            # User is interested in males, filter profiles for male users
            profiles = PersonalDetails.objects.exclude(user=request.user).filter(gender='M')
        elif user_details.interests == 'F':
            # User is interested in females, filter profiles for female users
            profiles = PersonalDetails.objects.exclude(user=request.user).filter(gender='F')
        else:
            # User is interested in both genders, no additional gender filter
            profiles = PersonalDetails.objects.exclude(user=request.user)

        if profiles.exists():
            # Select a random profile based on filtered criteria
            random_profile = random.choice(profiles)
            
            # Calculate the distance between the logged-in user and the random profile
            distance = user_details.calculate_distance(random_profile)

            profile_data = {
                'name': f'{random_profile.user.username} - {random_profile.get_age()}',
                'distance': f'{distance:.2f} km near you' if distance is not None else 'Distance not available',
            }

            if random_profile.profile_pic:
                profile_data['image_url'] = random_profile.profile_pic.url

            return JsonResponse(profile_data)
        else:
            return JsonResponse({'error': 'No profiles available'}, status=404)