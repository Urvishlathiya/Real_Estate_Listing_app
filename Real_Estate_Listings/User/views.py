from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, OTP
from .serializers import UserSerializer
from django.core.mail import send_mail  
import random


@api_view(["GET"])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def user_add(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def user_delete(request):
    user_entered_pk = request.headers.get("pk1")
    try:
        user = User.objects.get(pk=user_entered_pk)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
#-----------------------------------OTP-----------------------------


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import User, OTP
from Real_Estate_Listings.settings import generate_otp, send_otp_via_email  

@api_view(["POST"])
def generate_otp_view(request):
    email = request.data.get('email')
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    otp_code = generate_otp()

    otp = OTP(user=user, otp_code=otp_code)
    otp.save()
    success, message = send_otp_via_email(
        settings.EMAIL_HOST_USER, user.email, settings.EMAIL_HOST_PASSWORD, otp_code
    )

    if success:
        return Response({"message": "OTP sent to your email"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def verify_otp_view(request):
    email = request.data.get('email')
    otp_code = request.data.get('otp_code')

    try:
        user = User.objects.get(email=email)
        otp = OTP.objects.filter(user=user, otp_code=otp_code).latest('created_at')
        if otp.is_valid():
            user.is_verified = True
            user.save()
            return Response({"message": "OTP verified, user is now verified"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "OTP has expired"}, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response({"error": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except OTP.DoesNotExist:
        return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
    
    