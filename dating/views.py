from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
from .models import MatchRequest, Shortlist, Contacted, ProfileView, Story
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomPasswordChangeForm
from django.urls import reverse_lazy


class SelectgenderView(TemplateView):
    template_name = "Dating/selectgender.html"


def TestView(request):
    return render(request, "index.html")


# Group
class CreateGroupView(TemplateView):
    template_name = "groups/create_group.html"


class GroupListView(TemplateView):
    template_name = "groups/groups.html"


# SubscriptionPlan
class SubscriptionPlanView(TemplateView):
    template_name = "payment/subscription_plans.html"


class PaymentMethodsView(TemplateView):
    template_name = "payment/payment_methods.html"


class AddPaymentMethodsView(TemplateView):
    template_name = "payment/add_payment.html"


# G2
class StoryDetailView(DetailView):
    model = Story
    template_name = "User_profile/story.html"
    context_object_name = "story"

    def get_queryset(self):
        # Customize the queryset to filter active stories, etc.
        return Story.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["other_stories"] = Story.objects.exclude(pk=self.object.pk)[
            :5
        ]  # Example: Include additional stories
        return context


class ChangePasswordView(LoginRequiredMixin,PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy("home")
    template_name = "User_profile/change_password.html"


# here


class UserProfileView(DetailView):
    model = CustomUser
    template_name = "User_profile/user_profile.html"
    context_object_name = "profile_user"

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs["username"])


class SendRequestView(LoginRequiredMixin, View):
    def post(self, request, username):
        receiver = get_object_or_404(CustomUser, username=username)
        sender = request.user

        # Prevent sending request to self
        if sender == receiver:
            return redirect("profile", username=username)

        # Check if a request already exists
        match_request, created = MatchRequest.objects.get_or_create(
            sender=sender, receiver=receiver
        )
        if created:
            # New request sent
            # Optionally, send a notification or email
            pass
        else:
            # Request already exists
            pass

        return redirect("profile", username=username)


class ReceiveRequestView(LoginRequiredMixin, ListView):
    model = MatchRequest
    template_name = "contents/received_request.html"
    context_object_name = "received_requests"

    def get_queryset(self):
        return MatchRequest.objects.filter(receiver=self.request.user, status="sent")


class SendMatchRequestView(View):
    def post(self, request, username):
        recipient = get_object_or_404(CustomUser, username=username)
        MatchRequest.objects.get_or_create(sender=request.user, receiver=recipient)
        return redirect("profile", username=username)


class AcceptRequestView(LoginRequiredMixin, View):
    def post(self, request, request_id):
        match_request = get_object_or_404(
            MatchRequest, id=request_id, receiver=request.user
        )
        match_request.status = "accepted"
        match_request.save()
        # Optionally, create a mutual match or notify the sender
        return redirect("received_requests")


class RejectRequestView(LoginRequiredMixin, View):
    def post(self, request, request_id):
        match_request = get_object_or_404(
            MatchRequest, id=request_id, receiver=request.user
        )
        match_request.status = "rejected"
        match_request.save()
        return redirect("received_requests")


class ShortlistView(LoginRequiredMixin, View):
    def post(self, request, username):
        shortlisted_user = get_object_or_404(CustomUser, username=username)
        Shortlist.objects.get_or_create(
            user=request.user, shortlisted_user=shortlisted_user
        )
        return redirect("profile", username=username)


class ContactUserView(LoginRequiredMixin, View):
    def post(self, request, username):
        contacted_user = get_object_or_404(CustomUser, username=username)
        Contacted.objects.get_or_create(
            user=request.user, contacted_user=contacted_user
        )
        # Optionally, send notification or email
        return redirect("profile", username=username)


class UpgradeStoryView(TemplateView):
    template_name = "User_profile/upgrade_view_story.html"


class EditMyProfile(TemplateView):
    template_name = "User_profile/edite_my_profile.html"


def settings(request):
    return render(request, "User_profile/settings.html")


def privacy_settings(request):
    return render(request, "User_profile/privacy_settings.html")


def preferences(request):
    return render(request, "User_profile/preference.html")


def filter(request):
    return render(request, "User_profile/filter.html")


def user_profile(request):
    return render(request, "User_profile/user_profile.html")


def sent(request):
    return render(request, "contents/sent.html")


def accept(request):
    return render(request, "contents/accept.html")


def messgage(request):
    return render(request, "contents/message.html")


def contact(request):
    return render(request, "contents/contacted.html")


def shortlist(request):
    return render(request, "contents/shortlist.html")


def shortlist_by(request):
    return render(request, "contents/shortlist_by.html")


def received(request):
    return render(request, "contents/received.html")


def reject(request):
    return render(request, "contents/reject.html")


def viewed_myprofile(request):
    return render(request, "contents/viewed_myprofile.html")


#   G3
class Error403View(TemplateView):
    template_name = "error_page/error403.html"


class Error404View(TemplateView):
    template_name = "error_page/error404.html"


class HomeView(TemplateView):
    template_name = "Dating/home.html"


class DiscoverView(TemplateView):
    template_name = "Dating/discover.html"


class QualificationView(TemplateView):
    template_name = "Dating/qualification.html"


class LocationView(TemplateView):
    template_name = "Dating/location.html"


class DesignationView(TemplateView):
    template_name = "Dating/designation.html"


class MatchView(TemplateView):
    template_name = "Dating/matches.html"


class ProfileviewView(TemplateView):
    template_name = "Dating/profileviews.html"


class UpgradeView(TemplateView):
    template_name = "Dating/upgradepage.html"


class SpinView(TemplateView):
    template_name = "Dating/spin.html"
