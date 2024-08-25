from django.shortcuts import render
from django.views.generic import View, TemplateView


class SelectgenderView(TemplateView):
    template_name='Dating/selectgender.html'


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
