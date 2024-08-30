from django.contrib import admin
from .models import MatchRequest, Shortlist, Message, Contacted, ProfileView
# Register your models here.


admin.site.register(MatchRequest)
admin.site.register(Shortlist)
admin.site.register(Message)
admin.site.register(Contacted)
admin.site.register(ProfileView)
