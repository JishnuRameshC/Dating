from django.contrib import admin
from .models import CustomUser,OTP
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(OTP)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'mobile')
    actions = ['delete_selected']