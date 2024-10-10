from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Inquiry
from .serializers import InquirySerializer
from .models import User, Property  

@api_view(["POST"])
def create_inquiry(request):
    user_id = request.data.get('user_id')
    property_id = request.data.get('property_id')
    message = request.data.get('message')

    try:
        user = User.objects.get(id=user_id)
        property = Property.objects.get(id=property_id)
    except (User.DoesNotExist, Property.DoesNotExist):
        return Response({"error": "User or Property not found"}, status=status.HTTP_404_NOT_FOUND)

    inquiry = Inquiry(user=user, property=property, message=message)
    inquiry.save()

    serializer = InquirySerializer(inquiry)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def list_inquiries(request):
    inquiries = Inquiry.objects.all()
    serializer = InquirySerializer(inquiries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update_inquiry_status(request, inquiry_id):
    status_update = request.data.get('status')

    try:
        inquiry = Inquiry.objects.get(id=inquiry_id)
        if status_update in dict(Inquiry.INQUIRY_STATUS_CHOICES):
            inquiry.status = status_update
            inquiry.save()
            return Response({"message": "Inquiry status updated"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)
    except Inquiry.DoesNotExist:
        return Response({"error": "Inquiry not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["DELETE"])
def delete_inquiry(request, inquiry_id):
    try:
        inquiry = Inquiry.objects.get(id=inquiry_id)
        inquiry.delete()
        return Response({"message": "Inquiry deleted successfully"}, status=status.HTTP_200_OK)
    except Inquiry.DoesNotExist:
        return Response({"error": "Inquiry not found"}, status=status.HTTP_404_NOT_FOUND)

