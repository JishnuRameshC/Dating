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
    GENDER_CHOICES = [
      # This will be our placeholder
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
        # Add other options as needed
    ]
    INTERESTS_CHOICES = [
       # This will be our placeholder
        ('M', 'Male'),
        ('F', 'Female'),
        ('B', 'both'),
        # Add other options as needed
    ]

    SMOKING_CHOICES = [
        ('N', 'Never'),
        ('O', 'Occasionally'),
        ('F', 'Frequently'),
    ]
    
    DRINKING_CHOICES = [
        ('N', 'Never'),
        ('O', 'Occasionally'),
        ('F', 'Frequently'),
    ]
    
    
    QUALIFICATION_CHOICES = [
        ('SSLC', 'SSLC'),
        ('+2', 'Plus Two'),
        ('diploma', 'Diploma'),
        ('degree', 'Degree'),
        ('PG', 'Postgraduate'),
        ('PHD', 'PhD'),
    ]
    
    
    
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'p_details-input'})
    )
    interests = forms.ChoiceField(
        choices=INTERESTS_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'p_details-input'})
    )
    smoking_habits = forms.ChoiceField(
        choices=SMOKING_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'p_details-input'})
    )
    drinking_habits = forms.ChoiceField(
        choices=DRINKING_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'p_details-input'})
    )
    qualifications = forms.ChoiceField(
        choices=QUALIFICATION_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'p_details-input'})
    )

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
        
        # Ensure the first option (placeholder) is disabled
        self.fields['gender'].widget.choices[0] = ('', {'label': 'gender', 'disabled': True})
        self.fields['interests'].widget.choices[0] = ('', {'label': 'interests', 'disabled': True})
        self.fields['smoking_habits'].widget.choices[0] = ('', {'label': 'smoking_habits', 'disabled': True})
        self.fields['drinking_habits'].widget.choices[0] = ('', {'label': 'drinking_habits', 'disabled': True})
        self.fields['qualifications'].widget.choices[0] = ('', {'label': 'qualifications', 'disabled': True})
        
        # You can add more field customizations here if needed
        # For example:
        # self.fields['hobbies'].widget.attrs.update({'class': 'p_details-input'})
class AdditionalImageForm(forms.ModelForm):
    class Meta:
        model = AdditionalImage
        fields = ['image']  # Assuming 'images' is a ManyToManyField in your model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'multiple': True})
