from django.db import models
import uuid
from User.models import User  
from Properties.models import Property  

class Review(models.Model):
    REVIEW_CHOICES = [
        (1, 'Very Bad'),
        (2, 'Bad'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    property = models.ForeignKey(Property, on_delete=models.CASCADE)  
    rating = models.IntegerField(choices=REVIEW_CHOICES)
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.property.name}"
