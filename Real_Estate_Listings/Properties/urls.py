from django.urls import path
from .views import *

urlpatterns = [
    path('properties/', property_list),
    path('property_add/', property_add),
    path('properties/<uuid:pk>/', property_detail),
    path('properties/<uuid:pk>/update/', property_update),
    path('properties/<uuid:pk>/delete/', property_delete),
]
