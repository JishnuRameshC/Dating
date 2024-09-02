from django.contrib import admin
from .models import MatchRequest, Shortlist,Contacted,Message,ProfileView
admin.site.register(ProfileView)
admin.site.register(MatchRequest)
admin.site.register(Shortlist)
admin.site.register(Contacted)
admin.site.register(Message)


