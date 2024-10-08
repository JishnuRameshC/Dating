from django import forms

class FilterPreferencesForm(forms.Form):
    age_min = forms.IntegerField(required=False, initial=18)
    age_max = forms.IntegerField(required=False, initial=35)
    gender = forms.ChoiceField(choices=[('any', 'Any'), ('M', 'Male'), ('F', 'Female'), ('O', 'Others')], required=False)
    location = forms.CharField(required=False)
    hobbies = forms.CharField(required=False)
    occupation = forms.ChoiceField(
        choices=[('any', 'Any'), ('student', 'Student'), ('professional', 'Professional'), ('entrepreneur', 'Entrepreneur')],
        required=False
    )
    religion = forms.ChoiceField(
        choices=[('any', 'Any'), ('christianity', 'Christianity'), ('islam', 'Islam'), ('hinduism', 'Hinduism'), ('buddhism', 'Buddhism'), ('judaism', 'Judaism'), ('atheism', 'Atheism')],
        required=False
    )

class UserFilterForm(forms.Form):
    SORT_CHOICES = [
        ('newest', 'Newest Members'),
        ('last_active', 'Last Active'),
        ('distance', 'Distance'),
        ('popularity', 'Popularity'),
        ('age', 'Age')
    ]

    GENDER_CHOICES = [('any', 'Any'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    RELATIONSHIP_CHOICES = [('long_term', 'Long Term'), ('short_term', 'Short Term')]

    sort_by = forms.ChoiceField(choices=SORT_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    # CharField to accept multiple locations as a comma-separated string
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    hobbies = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    languages_spoken = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    relationship_goals = forms.ChoiceField(choices=RELATIONSHIP_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))