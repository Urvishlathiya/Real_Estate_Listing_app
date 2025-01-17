from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer


@api_view(["GET", "POST"])
def review_list_create(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)
    except Review.DoesNotExist:
        return Response({"message": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        review.delete()
        return Response({"message": "Review deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
