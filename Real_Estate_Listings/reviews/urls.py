from django.urls import path
from views import *

urlpatterns = [
    path('reviews/', review_list_create),
    path('reviews/<uuid:review_id>/',review_detail),
]
