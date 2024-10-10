from django.urls import path
from .views import *


urlpatterns = [
    path("user_list/", user_list),
    path("user_add/", user_add),
    path("user_delete/", user_delete)

]


urlpatterns = [
    path('generate-otp/', generate_otp_view),
    path('verify-otp/', verify_otp_view),
]
