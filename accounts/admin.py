from django.contrib import admin
from .models import CustomUser, AdditionalImage,Address,PersonalDetails,JobProfile
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(AdditionalImage)
admin.site.register(Address)
admin.site.register(PersonalDetails)
admin.site.register(JobProfile)