from django.contrib import admin
from .models import CustomUser, AdditionalImage,Address
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(AdditionalImage)
admin.site.register(Address)