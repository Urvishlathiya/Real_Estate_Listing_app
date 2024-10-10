from django.urls import path
from .views import *

urlpatterns = [
    path('inquiries/', list_inquiries),
    path('create_inquiry/', create_inquiry),
    path('inquiries/update/<uuid:inquiry_id>/', update_inquiry_status),
    path('inquiries/delete/<uuid:inquiry_id>/',delete_inquiry),
]
