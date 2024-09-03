from django.db import models

from django.db import models
from accounts.models import CustomUser
# Create your models here.


class MatchRequest(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('received', 'Received'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey(CustomUser, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sent')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f'{self.sender} -> {self.receiver} ({self.status})'



class Shortlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='shortlisted_by', on_delete=models.CASCADE)
    shortlisted_user = models.ForeignKey(CustomUser, related_name='shortlisted', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.user} shortlisted {self.shortlisted_user}'

class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def _str_(self):
        return f'Message from {self.sender} to {self.receiver} at {self.timestamp}'

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='contacts_made', on_delete=models.CASCADE)
    contacted_user = models.ForeignKey(CustomUser, related_name='contacts_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.user} contact{self.contacted_user}'


class ProfileView(models.Model):
    id = models.BigAutoField(primary_key=True)
    viewer = models.ForeignKey(CustomUser, related_name='profile_views', on_delete=models.CASCADE)
    viewed_user = models.ForeignKey(CustomUser, related_name='viewed_by', on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.viewer} viewed {self.viewed_user} profile at {self.viewed_at}'