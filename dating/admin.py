from django.contrib import admin
from . models import MatchRequest, Shortlist, Contacted, ProfileView, Story, Comment
# from .models import MatchRequest, Shortlist, Contacted, ProfileView
# # Register your models here.

admin.site.register(MatchRequest)
admin.site.register(Shortlist)
admin.site.register(Contacted)
admin.site.register(ProfileView)
admin.site.register(Story)
admin.site.register(Comment)
# admin.site.register(MatchRequest)
# admin.site.register(Shortlist)

# admin.site.register(Contacted)
# admin.site.register(ProfileView)
