from django.shortcuts import render


# Create your views here.

def TestView(request):
    return render(request, 'index.html')

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
