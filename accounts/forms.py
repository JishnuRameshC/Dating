from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import AdditionalImage, CustomUser, JobProfile,PersonalDetails

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'mobile', 'password1', 'password2']

    


class PersonalDetailsForm(forms.ModelForm):
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
    RELIGION_CHOICES=[
        ('christianity','christianity'),
        ('islam','islam'),
        ('hindhuism','hindhuism'),
        ('judaism','judaism'),
        ('atheism','atheism'),
        ('other','other'),
    ]
    
    
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'p_details-input'})
    )
    religion = forms.ChoiceField(
        choices=RELIGION_CHOICES,
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
        model = PersonalDetails
        fields = [
            'gender', 'dob','religion', 'hobbies', 'interests', 
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


class JobProfileForm(forms.ModelForm):
    class Meta:
        model = JobProfile
        fields = ['job_status']
        
class EmployerDetailsForm(forms.ModelForm):
    class Meta:
        model = JobProfile
        fields = [
            'company_name', 
            'designation', 
            'location', 
            
            
            
        ]
        
class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model=JobProfile
        fields=[
            'job_title',
            'expertise_level'
            ]
        
class RelationshipGoalsForm(forms.ModelForm):
    class Meta:
        model=PersonalDetails
        fields=[
            'relationship_goals'
        ]