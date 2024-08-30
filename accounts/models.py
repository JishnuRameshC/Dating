from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    HABITS_CHOICES = [
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
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True, blank=True, null=True)

    # Personal Details fields
    age = models.PositiveIntegerField(null=True, blank=True, default=None)
    dob = models.DateField(null=True, blank=True, default=None)
    hobbies = models.CharField(max_length=255, blank=True, default='')
    interests = models.CharField(max_length=255, blank=True, default='')
    smoking_habits = models.CharField(max_length=50, choices=HABITS_CHOICES, blank=True, default='')
    drinking_habits = models.CharField(max_length=50, choices=HABITS_CHOICES, blank=True, default='')
    qualifications = models.CharField(max_length=255, blank=True, default='')
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default='')
    additional_images = models.ManyToManyField('AdditionalImage', blank=True)
    short_reel = models.FileField(upload_to='short_reels/', null=True, blank=True, default='')

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

    def __str__(self):
        return self.username
    

class AdditionalImage(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE ,default=None)
    image = models.ImageField(upload_to='additional_images/')

    def __str__(self):
        return f"Image {self.id}"


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