from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import AdditionalImage, CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'mobile', 'password1', 'password2']

    


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
        # Example: Set custom class for fields
          

class AdditionalImageForm(forms.ModelForm):
    class Meta:
        model = AdditionalImage
        fields = ['image']  # Assuming 'images' is a ManyToManyField in your model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'multiple': True})
