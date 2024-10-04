from django.contrib import admin

from .models import Shortlist,ProfileView,FriendRequest,Story,Comment
admin.site.register(ProfileView)
admin.site.register(Shortlist)
admin.site.register(FriendRequest)
admin.site.register(Story)
admin.site.register(Comment)





