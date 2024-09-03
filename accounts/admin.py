from django.contrib import admin
from .models import CustomUser,JobProfile,PersonalDetails
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(JobProfile)
admin.site.register(PersonalDetails)


