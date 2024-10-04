
from django.db import models
from accounts.models import CustomUser
from django.db import models
from accounts.models import CustomUser

class Story(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return f"Story by {self.user.username} at {self.created_at}"

class Comment(models.Model):
    story = models.ForeignKey(Story, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return f"Comment by {self.user.username} on {self.story} at {self.created_at}"


class FriendRequest(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),         # When a request is sent but not yet accepted or rejected
        ('accepted', 'Accepted'), # When the receiver accepts the request
        ('rejected', 'Rejected'), # When the receiver rejects the request
        ('contacted', 'Contacted')# When users establish contact after accepting
    ]
    sender = models.ForeignKey(CustomUser, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sent')
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.sender} -> {self.receiver} [{self.get_status_display()}]"



class Shortlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='shortlisted_by', on_delete=models.CASCADE)
    shortlisted_user = models.ForeignKey(CustomUser, related_name='shortlisted', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.user} shortlisted {self.shortlisted_user}'
    


class ProfileView(models.Model):
    id = models.BigAutoField(primary_key=True)
    viewer = models.ForeignKey(CustomUser, related_name='profile_views', on_delete=models.CASCADE)
    viewed_user = models.ForeignKey(CustomUser, related_name='viewed_by', on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.viewer} viewed {self.viewed_user} profile at {self.viewed_at}'