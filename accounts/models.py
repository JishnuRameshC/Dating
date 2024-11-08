from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.distance import geodesic
from django.utils import timezone
from datetime import timedelta


class CustomUser(AbstractUser):
    
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True, blank=True, null=True)

    last_activity = models.DateTimeField(null=True, blank=True)  # Track last activity

    
    # Overriding fields for custom behavior
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Unique related_name for CustomUser
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Unique related_name for CustomUser
        blank=True,
    )
    


    def update_last_activity(self):
        self.last_activity = timezone.now()
        self.save()

    def is_online(self):
        if self.last_activity:
            return timezone.now() - self.last_activity <= timedelta(minutes=2)
        return False

    
    def __str__(self):
        return self.username
    
    
class PersonalDetails(models.Model):
    HABITS_CHOICES = [
        ('N', 'Never'),
        ('O', 'Occasionally'),
        ('F', 'Frequently'),
    ]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    INTEREST_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('B', 'Both'),
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
    RELATIONSHIP_CHOICES=[
        ('long_term','short_term'),
        ('short_term','short_term')
    ]
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender=models.CharField(max_length=25,choices=GENDER_CHOICES,blank=True, default='')
    dob = models.DateField(null=True, blank=True, default=None)
    religion=models.CharField(max_length=25,null=True,blank=True,default='')
    hobbies = models.CharField(max_length=255, blank=True, default='')
    interests = models.CharField(max_length=25,choices=INTEREST_CHOICES, blank=True, default='')
    smoking_habits = models.CharField(max_length=25, choices=HABITS_CHOICES, blank=True, default='')
    drinking_habits = models.CharField(max_length=25, choices=HABITS_CHOICES, blank=True, default='')
    qualifications = models.CharField(max_length=25,choices=QUALIFICATION_CHOICES, blank=True, default='')
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default='')
    additional_images = models.ManyToManyField('AdditionalImage', blank=True)
    short_reel = models.FileField(upload_to='short_reels/', null=True, blank=True, default='')
    relationship_goals=models.CharField(max_length=25,choices=RELATIONSHIP_CHOICES,blank=True,null=True,default='')
    
    def get_age(self):
        if self.dob:
            today = date.today()
            age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
            return age
        return None
      
    def calculate_match_score(self, other_user_details):
        score = 0
        
        # Match gender with interests
        if self.gender and other_user_details.interests:
            if self.gender == other_user_details.interests or other_user_details.interests == 'B':
                score += 30

        if other_user_details.gender and self.interests:
            if other_user_details.gender == self.interests or self.interests == 'B':
                score += 20

        # Match age within a range of 5 years
        if self.get_age() and other_user_details.get_age():
            age_difference = abs(self.get_age() - other_user_details.get_age())
            if age_difference <= 5:
                score += 10

        # Match religion
        if self.religion and self.religion == other_user_details.religion:
            score += 10

        # Match smoking habits
        if self.smoking_habits == other_user_details.smoking_habits:
            score += 5

        # Match drinking habits
        if self.drinking_habits == other_user_details.drinking_habits:
            score += 5

        # Match relationship goals
        if self.relationship_goals == other_user_details.relationship_goals:
            score += 10

        if self.qualifications and other_user_details.qualifications:
            if self.qualifications == other_user_details.qualifications:
                score += 10

        return score

    def calculate_distance(self, other_user_details):
        my_address = self.user.address_set.filter(is_default=True).first()
        other_address = other_user_details.user.address_set.filter(is_default=True).first()

        # Ensure both addresses are valid
        if my_address and other_address:
            my_coords = my_address.get_coordinates_from_address_line_3()
            other_coords = other_address.get_coordinates_from_address_line_3()

            if my_coords and other_coords:
                return geodesic(my_coords, other_coords).km
        return None 
    
    def __str__(self) -> str:
        return self.user.username
    


class AdditionalImage(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE ,default=None)
    image = models.ImageField(upload_to='additional_images/')



class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250)
    address_line_3 = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'name']

    def __str__(self) -> str:
        return f'''
            {self.address_line_1}
            {self.address_line_2}
            {self.address_line_3}
            {self.city}
            {self.state}
            {self.country}
            '''
            

    def get_coordinates_from_address_line_3(self):
        
        geolocator = Nominatim(user_agent="accounts")
        if self.address_line_3:
            try:
                location = geolocator.geocode(self.address_line_3)
                if location:
                    return (location.latitude, location.longitude)
            except GeocoderTimedOut:
                return None
        return None


class JobProfile(models.Model):
    STATUS_CHOICES = [
        ('employer', 'Employer'),
        ('employee', 'Employee'),
        ('job_seeker', 'Job Seeker'),
    ]

    EXPERTISE_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    ]
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    job_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    designation=models.CharField(max_length=100,blank=True,null=True,default='')
    location = models.CharField(max_length=255, blank=True, null=True)
    job_title=models.CharField(max_length=100,blank=True,null=True,default='')
    expertise_level = models.CharField(max_length=20, choices=EXPERTISE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f" {self.user.username}_{self.get_job_status_display()}"
    
