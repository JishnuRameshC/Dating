from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import AdditionalImage, CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'mobile', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if mobile and CustomUser.objects.filter(mobile=mobile).exists():
            raise ValidationError("A user with this mobile number already exists.")
        return mobile

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'gender', 'dob', 'hobbies', 'interests', 
            'smoking_habits', 'drinking_habits', 
            'qualifications', 'profile_pic', 'short_reel'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
        def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
           # Provide initial values if any

class AdditionalImageForm(forms.ModelForm):
    class Meta:
        model = AdditionalImage
        fields = ['image']  # Assuming 'images' is a ManyToManyField in your model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'multiple': True})
