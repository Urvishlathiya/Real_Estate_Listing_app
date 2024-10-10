from django.db import models
import uuid
from django.utils import timezone
from User.models import User
from Properties.models import Property

class Inquiry(models.Model):
    INQUIRY_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    message = models.TextField() 
    status = models.CharField(max_length=10, choices=INQUIRY_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inquiry by {self.user.username} on {self.property.title}"
