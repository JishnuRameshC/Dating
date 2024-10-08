from django.contrib import admin
from .models import CustomUser,JobProfile,PersonalDetails,Address
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(JobProfile)
admin.site.register(PersonalDetails)
admin.site.register(Address)