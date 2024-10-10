from django.db import models
import uuid
from User.models import User

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('commercial', 'Commercial'),
        ('land', 'Land'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100) 
    description = models.TextField()  
    type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES) 
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)  
    state = models.CharField(max_length=50)  
    zip_code = models.CharField(max_length=10)  
    country = models.CharField(max_length=50, default="India")  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    area_in_sqft = models.DecimalField(max_digits=7, decimal_places=2)  
    bedrooms = models.IntegerField(null=True, blank=True)  
    bathrooms = models.IntegerField(null=True, blank=True)  
    parking_spaces = models.IntegerField(null=True, blank=True)  
    is_available = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    modified_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title

