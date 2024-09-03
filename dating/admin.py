from django.contrib import admin

from .models import MatchRequest,Shortlist,Contact,Message,ProfileView
admin.site.register(ProfileView)
admin.site.register(MatchRequest)
admin.site.register(Shortlist)
admin.site.register(Contact)
admin.site.register(Message)


