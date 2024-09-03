from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Story, Comment

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter current password',
            'id': 'current-password'
        }),label="Current password"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter new password',
            'id': 'new-password'
        }),label="New password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm new password',
            'id': 'confirm-password'
        }),label="Confirm new password"
    )


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('caption',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


# class UserSearchForm(forms.Form):
#     gender = forms.ChoiceField(choices=[('', 'Any')] + CustomUser.GENDER_CHOICES, required=False)
#     min_age = forms.IntegerField(min_value=18, required=False)
#     max_age = forms.IntegerField(min_value=18, required=False)
#     interests = forms.ChoiceField(choices=[('', 'Any')] + CustomUser.INTEREST_CHOICES, required=False)
