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

