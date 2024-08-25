from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def TestView(request):
    return render(request, 'index.html')


class StoryPageView(TemplateView):
    template_name = 'story.html'


class ChangePasswordView(TemplateView):
    template_name = 'change_password.html'


# class ProfileView(TemplateView):
#     template_name = 'user_profile.html'


class UpgradeStoryView(TemplateView):
    template_name = 'upgrade_view_story'


class EditMyProfile(TemplateView):
    template_name = 'edite_my_profile.html'